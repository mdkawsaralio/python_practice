def selection_sort(arr):
  n=len(arr)
  for i in range(n-1):   # initializing the loop for n-1 times n=4
    min_index=i         # initializing the minimum index with the current index
    for j in range(i+1,n):      # initializing the loop for i+1 to n times
      if arr[j]<arr[min_index]:  # comparing the current element with the minimum index element 
        min_index=j              # updating the minimum index if a smaller element is found
    arr[i],arr[min_index]=arr[min_index],arr[i]   #swapping the current element with the minimum index element
  return arr


print(selection_sort([10,2,3,4,5]))

# Selection Sort অ্যালগরিদমে প্রতিটি পাসে (pass) অ্যারের unsorted অংশ থেকে সবচেয়ে ছোট (minimum) উপাদানটি খুঁজে বের করা হয় এবং সেটিকে বর্তমান অবস্থান (i) এর সাথে একবার swap করা হয়। ধরা যাক arr = [10, 2, 3, 4, 5]। প্রথমে n = len(arr) = 5। বাইরের লুপ for i in range(n-1) মোট ৪ বার চলে (i = 0, 1, 2, 3)। প্রথম পাসে (i = 0) min_index = 0 ধরা হয়, অর্থাৎ 10-কে আপাতত সবচেয়ে ছোট ধরা হয়। এরপর ভেতরের লুপ j = 1, 2, 3, 4 পর্যন্ত চলে এবং 2-কে সবচেয়ে ছোট সংখ্যা হিসেবে খুঁজে পায়। তাই min_index = 1 হয়। ভেতরের লুপ শেষ হলে 10 ও 2 একবার swap করা হয় এবং অ্যারে হয় [2, 10, 3, 4, 5]।

# দ্বিতীয় পাসে (i = 1) min_index = 1 অর্থাৎ 10 ধরা হয়। এরপর 3, 4 এবং 5-এর সাথে তুলনা করে দেখা যায় 3 সবচেয়ে ছোট। তাই min_index = 2 হয়। ভেতরের লুপ শেষ হলে 10 ও 3 swap করা হয় এবং অ্যারে হয় [2, 3, 10, 4, 5]। তৃতীয় পাসে (i = 2) 10-এর সাথে 4 ও 5 তুলনা করা হয়। 4 সবচেয়ে ছোট হওয়ায় min_index = 3 হয় এবং শেষে swap করে অ্যারে হয় [2, 3, 4, 10, 5]। চতুর্থ পাসে (i = 3) 10 ও 5 তুলনা করা হয়। 5 ছোট হওয়ায় min_index = 4 হয় এবং শেষে swap করলে চূড়ান্ত সাজানো অ্যারে হয় [2, 3, 4, 5, 10]।

# Selection Sort-এ প্রতিটি পাসে শুধুমাত্র একটি swap করা হয়, কিন্তু পুরো unsorted অংশে minimum উপাদান খুঁজতে একাধিক comparison করা হয়। তাই ৫টি উপাদানের ক্ষেত্রে মোট comparison হয় ৪ + ৩ + ২ + ১ = ১০টি, আর swap হয় সর্বোচ্চ ৪টি। এটাই Selection Sort-এর প্রধান বৈশিষ্ট্য।

