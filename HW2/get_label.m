load digitStruct.mat
for i = 1: length(digitStruct)
    im = imread([digitStruct(i).name]);
    filename = digitStruct(i).name;
    filename = convertCharsToStrings(filename);
    filename = split(filename, ["."]);
    path = "./label/";
    txt_name = path + filename(1) + ".txt";
    fid = fopen(txt_name, 'w');
    %fprintf(fid, txt_name);

    for j = 1:length(digitStruct(i).bbox)
        [total_height, total_width, channel] = size(im);
        x_center = digitStruct(i).bbox(j).left + (digitStruct(i).bbox(j).width / 2);
        x_center = x_center / total_width;
        y_center = digitStruct(i).bbox(j).top + (digitStruct(i).bbox(j).height / 2);
        y_center = y_center / total_height;
        height = digitStruct(i).bbox(j).height;
        height = height / total_height;
        width = digitStruct(i).bbox(j).width;
        width = width / total_width;
        label = digitStruct(i).bbox(j).label;
        if (label == 10)
            label = 0;
        end
        fprintf(fid, '%d %f %f %f %f\n', label, x_center, y_center, width, height);
    end
    fclose(fid);
end
fprintf("done");
