import argparse
import time
import os
import imageio
import options.options as option
from utils import util
from solvers import create_solver
from data import create_dataloader
from data import create_dataset


def main():
    help_str = 'Test Super Resolution Models'
    parser = argparse.ArgumentParser(description=help_str)
    help_str = 'Path to options JSON file.'
    parser.add_argument('-opt', type=str, required=True, help=help_str)
    opt = option.parse(parser.parse_args().opt)
    opt = option.dict_to_nonedict(opt)

    # initial configure
    scale = opt['scale']
    degrad = opt['degradation']
    network_opt = opt['networks']
    model_name = network_opt['which_model'].upper()
    if opt['self_ensemble']:
        model_name += 'plus'

    # create test dataloader
    bm_names = []
    test_loaders = []
    for _, dataset_opt in sorted(opt['datasets'].items()):
        test_set = create_dataset(dataset_opt)
        test_loader = create_dataloader(test_set, dataset_opt)
        test_loaders.append(test_loader)
        print('===> Test Dataset: [%s]' % (test_set.name()))
        print('Number of images: [%d]' % (len(test_set)))
        bm_names.append(test_set.name())

    # create solver (and load model)
    solver = create_solver(opt)
    # Test phase
    print('===> Start Test')
    print("==================================================")
    print("Method: %s " % (model_name))
    print('Scale: %d || Degradation: %s' % (scale, degrad))

    for bm, test_loader in zip(bm_names, test_loaders):
        print("Test set : [%s]" % bm)

        sr_list = []
        path_list = []

        total_psnr = []
        total_ssim = []
        total_time = []
        if test_loader.dataset.__class__.__name__.find('LRHR') < 0:
            need_HR = False  
        else:
            need_HR = True

        for iter, batch in enumerate(test_loader):
            solver.feed_data(batch, need_HR=need_HR)

            # calculate forward time
            t0 = time.time()
            solver.test()
            t1 = time.time()
            total_time.append((t1 - t0))

            visuals = solver.get_current_visual(need_HR=need_HR)
            sr_list.append(visuals['SR'])

            # calculate PSNR/SSIM metrics on Python
            if need_HR:
                psnr, ssim = util.calc_metrics(visuals['SR'], visuals['HR'], crop_border=scale)
                total_psnr.append(psnr)
                total_ssim.append(ssim)
                path_list.append(os.path.basename(batch['HR_path'][0]).replace('HR', model_name))
                print("[%d/%d] %s || PSNR(dB)/SSIM: %.2f/%.4f || Timer: %.4f sec ." % (iter+1, len(test_loader),
                                                                                       os.path.basename(batch['LR_path'][0]),
                                                                                       psnr, ssim,
                                                                                       (t1 - t0)))
            else:
                path_list.append(os.path.basename(batch['LR_path'][0]))
                print("[%d/%d] %s || Timer: %.4f sec ." % (iter + 1, len(test_loader),
                                                           os.path.basename(batch['LR_path'][0]),
                                                           (t1 - t0)))

        if need_HR:
            print("---- Average PSNR(dB) /SSIM /Speed(s) for [%s] ----" % bm)
            print("PSNR: %.2f      SSIM: %.4f      Speed: %.4f" % (sum(total_psnr)/len(total_psnr),
                                                                  sum(total_ssim)/len(total_ssim),
                                                                  sum(total_time)/len(total_time)))
        else:
            print("---- Average Speed(s) for [%s] is %.4f sec ----" % (bm,
                                                                      sum(total_time)/len(total_time)))

        # save SR results for further evaluation on MATLAB
        if need_HR:
            save_img_path = os.path.join('./results/SR/'+degrad, model_name, bm, "x%d"%scale)
        else:
            save_img_path = os.path.join('./results/SR/'+bm, model_name, "x%d"%scale)

        print("===> Saving SR images of [%s]... Save Path: [%s]\n" % (bm, save_img_path))

        if not os.path.exists(save_img_path): os.makedirs(save_img_path)
        for img, name in zip(sr_list, path_list):
            file_name=name.split(".png")[0]+"_pred.png"
            print(file_name)
            imageio.imwrite(os.path.join(save_img_path, file_name), img)

    print("==================================================")
    print("===> Finished !")

if __name__ == '__main__':
    main()