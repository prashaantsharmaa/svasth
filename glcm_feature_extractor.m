
files = dir('*.png');
% cnt = 0;

for file = files'
    img = imread(file.name);
    input = rgb2gray(img)

    offsets = [0 1; -1 1;-1 0;-1 -1];

    glcm = graycomatrix(input, 'Offset', offsets, 'Symmetric', true)

    stats = graycoprops(glcm)

    contrast = stats.Contrast
    correlation = stats.Correlation
    energy = stats.Energy
    homogeneity = stats.Homogeneity
    entropy = Entropy(img)
    
   % cnt = cnt + 1;
   % filename = file.name;

    feature_vec = [contrast correlation energy homogeneity entropy];


    fid = fopen('a_roi_features_preproc.txt','a');
    fprintf(fid,'%f ',feature_vec);
    fprintf(fid,'\n');
    fclose(fid);
end
