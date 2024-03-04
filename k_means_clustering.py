#!/usr/bin/python3
import numpy as np
import cv2 as cv

def assign_clusters(my_clusters,point_value):
    dist = []
    for ite in range(len(my_clusters)):
        dist.append(np.sqrt(np.sum((my_clusters[ite]-point_value[:3])**2, axis=0)))

    cluster_idx = np.argmin(dist)   
    return cluster_idx


def update_clusters(current_clusters,my_map):
    old_clusters = current_clusters.copy()

    for ite in range(current_clusters.shape[0]):
        temp = np.array(np.argwhere(my_map[:,:,3]==ite))
        brg_values = np.mean(my_map[temp[:,0],temp[:,1],:3],axis=0)
        current_clusters[ite] = brg_values

    
    if np.array_equal(old_clusters,current_clusters):
        flag_break = True
    else:
        flag_break = False
   
    return flag_break , current_clusters


def main():
    img=cv.imread('Media/image.jpeg')
    k1_cluster = [0,0,0]
    k2_cluster = [0,0,255]
    k3_cluster = [0,255,0]
    k4_cluster = [255,0,0]
    my_cluster = np.array([k1_cluster,k2_cluster,k3_cluster,k4_cluster])
    
    my_map = np.dstack((img,np.zeros((451, 612),dtype=np.uint8)))
    count = 0
    while True:
        
        for ix in range(my_map.shape[0]):
            for iy in range(my_map.shape[1]):
                my_map[ix,iy,3] = assign_clusters(my_cluster,my_map[ix,iy])


        flag_break , my_cluster = update_clusters(my_cluster,my_map)
        count +=1
        if flag_break:
            break
    display_each_cluster(img,my_map,my_cluster)
    

def display_each_cluster(img,my_map,my_cluster):
    final_cluster_1 = np.argwhere(my_map[:,:,3]==0)
    blank_cluster_1 = np.zeros_like(img)

    final_cluster_2 = np.argwhere(my_map[:,:,3]==1)
    blank_cluster_2 = np.zeros_like(img)

    final_cluster_3 = np.argwhere(my_map[:,:,3]==2)
    blank_cluster_3 = np.zeros_like(img)

    final_cluster_4 = np.argwhere(my_map[:,:,3]==3)
    blank_cluster_4 = np.zeros_like(img)

    for i in final_cluster_1:
        x,y = i.ravel()
        blank_cluster_1[x,y] = my_cluster[0][:]
        img[x,y] = my_cluster[0][:]
    cv.namedWindow('cluster 1', cv.WINDOW_NORMAL)
    cv.imshow('cluster 1',blank_cluster_1)
    cv.imwrite('Results/cluster1.jpg', blank_cluster_1)

    for i in final_cluster_2:
        x,y = i.ravel()
        blank_cluster_2[x,y] = my_cluster[1][:]
        img[x,y] = my_cluster[1][:]
    cv.namedWindow('cluster 2', cv.WINDOW_NORMAL)
    cv.imshow('cluster 2',blank_cluster_2)
    cv.imwrite('Results/cluster2.jpg', blank_cluster_2)

    for i in final_cluster_3:
        x,y = i.ravel()
        blank_cluster_3[x,y] = my_cluster[2][:]
        img[x,y] = my_cluster[2][:]
    cv.namedWindow('cluster 3', cv.WINDOW_NORMAL)
    cv.imshow('cluster 3',blank_cluster_3)
    cv.imwrite('Results/cluster3.jpg', blank_cluster_3)

    for i in final_cluster_4:
        x,y = i.ravel()
        blank_cluster_4[x,y] = my_cluster[3][:]
        img[x,y] = my_cluster[3][:]
    cv.namedWindow('cluster 4', cv.WINDOW_NORMAL)
    cv.imshow('cluster 4',blank_cluster_4)
    cv.imwrite('Results/cluster4.jpg', blank_cluster_4)

    cv.namedWindow('filtered image',cv.WINDOW_NORMAL)
    cv.imshow('filtered image',img)
    cv.imwrite('Results/result.jpg', img)
    cv.waitKey(0)


if __name__ =='__main__':
    main()

        