function [] = transfer(hdr_path,img_path)
    %read .hdr and .img file
    Info = analyze75info(hdr_path);
    Img = analyze75read(img_path);
    % Get the size of 3D image
    [m_height, m_width, m_thick] = size(Img);
    % Write dicom file, then we can use it in python(use pydicom)
    filename = '/Users/mikechen/Downloads/CT Image/CT_007_';
    % take each stack out
    % change name and save everything as .dcm file
    for i = 1:m_thick
        newname = [filename, int2str(i)];
        newname = [newname, '.dcm'];
        pp =Img(1:m_height,1:m_width,i);
        imshow(pp,[]);
        dicomwrite(pp,newname);
    end
end

