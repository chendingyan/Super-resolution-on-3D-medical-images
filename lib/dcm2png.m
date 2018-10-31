function [I] = dcm2png(filepath)

    list = dir(fullfile(filepath));
    for k = 3:size(list,1)
%         fprintf('%s',list(k).name);
        sublist = dir([filepath '/' list(k).name]);
        for n = 3:size(sublist)
%             fprintf('%s',sublist(k).name)
            dcmpath = [sublist(n).folder '/' sublist(n).name];
             I = dicomread(dcmpath)
             I=double(I)+128;
%              I=uint16(I);
             imshow(I,[]);
             dcmpath(end-2:end)=["png"];
             imwrite(I, dcmpath);
             
        end
    end

end

