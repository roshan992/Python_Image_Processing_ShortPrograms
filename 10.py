for i in range(0,nr,1):
    for j in range(0,nc,1):
        img2[i][j]=img1[nr-i-1][j];
        img3[i][j]=img1[nr-j-1][j];
