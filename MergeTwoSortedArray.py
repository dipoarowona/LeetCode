def MergeTwoSortedArray(nums1, m, nums2, n):
    x = 0
    for i in range(m,len(nums1)):
        nums1[i] = nums2[x]
        x+=1
    nums1.sort()
    return nums1 

print(MergeTwoSortedArray([4,5,6,0,0,0],3,[1,2,3],3))


def secondSol(nums1, m, nums2, n):
    #start from end and move to the beginning for all 3 pointers
    #end of nums1, end of nums2, at m-1 index of nums1
    end = len(nums1)

    #m and n become indexes of the respective lists
    m -=1
    n -=1

    for i in range(end-1,-1,-1):
        print(i)
        if m<0:
            nums1[i] = nums2[n]
            n-=1
        elif n<0:
            nums1[i] = nums1[m]
            m-=1
        else:
            if nums1[m] >= nums2[n]:
                nums1[i] = nums1[m]
                m-=1
            else:
                nums1[i] = nums2[n]
                n-=1

    return(nums1)

print(secondSol([4,5,6,0,0,0],3,[1,2,3],3))