# # ----------------Threading- kop oqimli------------
# import time
# import threading
#
#
# def generate_num():
#     for i in range(1, 11):
#         print(i)
#         time.sleep(1)
#
#
# start = time.time()
#
# th1 = threading.Thread(target=generate_num())
# th2 = threading.Thread(target=generate_num())
# th3 = threading.Thread(target=generate_num())
#
# th1.start()
# th2.start()
# th3.start()
# th1.join()
# th2.join()
# th3.join()
#
# end = time.time()
#
# print(f"dasrur ishlashi ucun {round(end-start), 2} sekund vaqt ketdi!")
# -------------------------
# import time
# import threading
#
#
# def generate_num():
#     Th1 = []
#     for i in range(1000):
#         th1 = threading.Thread(target=generate_num())
#         th1.start()
#         Th1.append(i)
#
#     for elem in Th1:
#         elem.join()
# end = time.time()
#
# print(f"dasrur ishlashi ucun {round(end-start), 2} sekund vaqt ketdi!")
# -----------------------------------------------------------
# import threading
# import time
# import requests
#
# img_urls = [
#     "https://images.unsplash.com/photo-1516117172878-fd2c41f4a759",
#     "https://images.unsplash.com/photo-1532009324734-20a7a5813719",
#     "https://images.unsplash.com/photo-1524429656589-6633a470097c",
#     "https://images.unsplash.com/photo-1530224264768-7ff8c1789d79",
#     "https://images.unsplash.com/photo-1564135624576-c5c88640f235",
#     "https://images.unsplash.com/photo-1541698444083-023c97d3f4b6",
#     "https://images.unsplash.com/photo-1522364723953-452d3431c267",
#     "https://images.unsplash.com/photo-1513938709626-033611b8cc03",
#     "https://images.unsplash.com/photo-1507143550189-fed454f93097",
#     "https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e",
#     "https://images.unsplash.com/photo-1504198453319-5ce911bafcde",
#     "https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99",
#     "https://images.unsplash.com/photo-1516972810927-80185027ca84",
#     "https://images.unsplash.com/photo-1550439062-609e1531270e",
#     "https://images.unsplash.com/photo-1549692520-acc6669e2f0c"
# ]
#
# def download_image(image_url: str):
#     image_name = image_url.split("/")[-1] + ".jpg"
#     request = requests.get(image_url)
#     if request.status_code == 200:
#         data = request.content
#         with open(f"images/{image_name}", "wb") as file:
#             file.write(data)
#         print(f"{image_name} yuhlandi!!!")
#     else:
#         print("numadir notogri ketdi!!!")
#
# start = time.time()
# ths = []
# # for img_url in img_urls:
# #     th = threading.Thread(target=download_image, args=(img_url,))
# #     th.start()
# #     ths.append(th)
# #
# # for th in ths:
# #     th.join()
#
# end = time.time()
# print(f"dasrur ishlashi ucun {round(end - start, 2)} sekund vaqt ketdi!")
# -------------------------------------------------
# import requests
# import time
# from concurrent import futures
#
#
# img_urls = [
#    'https://images.unsplash.com/photo-1516117172878-fd2c41f4a759',
#    'https://images.unsplash.com/photo-1532009324734-20a7a5813719',
#    'https://images.unsplash.com/photo-1524429656589-6633a470097c',
#    'https://images.unsplash.com/photo-1530224264768-7ff8c1789d79',
#    'https://images.unsplash.com/photo-1564135624576-c5c88640f235',
#    'https://images.unsplash.com/photo-1541698444083-023c97d3f4b6',
#    'https://images.unsplash.com/photo-1522364723953-452d3431c267',
#    'https://images.unsplash.com/photo-1513938709626-033611b8cc03',
#    'https://images.unsplash.com/photo-1507143550189-fed454f93097',
#    'https://images.unsplash.com/photo-1493976040374-85c8e12f0c0e',
#    'https://images.unsplash.com/photo-1504198453319-5ce911bafcde',
#    'https://images.unsplash.com/photo-1530122037265-a5f1f91d3b99',
#    'https://images.unsplash.com/photo-1516972810927-80185027ca84',
#    'https://images.unsplash.com/photo-1550439062-609e1531270e',
#    'https://images.unsplash.com/photo-1549692520-acc6669e2f0c'
# ]
#
#
# def download_image(image_url: str):
#     image_name = image_url.split("/")[-1] + ".jpg"
#     request = requests.get(image_url)
#     if request.status_code == 200:
#         data = request.content
#         with open(f"images/{image_name}", mode="wb") as file:
#             file.write(data)
#         print(f"{image_name} yuklandi✅")
#     else:
#         print("Qandaydir hatolik ketdi!!!")
#
#
# start = time.time()
#
# with futures.ThreadPoolExecutor() as executor:
#     executor.map(download_image, img_urls)
#
# end = time.time()
#
# print(f"Dastur ishlashi uchun {round(end-start, 2)} secund vaqt ketdi!")

#
# url = "https://api.alijonov.uz/api/namoz.php?city=fargona"
# request = requests.get(url)
# js = request.json()
#
# if request.status_code == 200:
#     print(f"Bomdod: {js['vaqtlar']['bomdod']}\n"
#           f"Quyosh: {js['vaqtlar']['quyosh']}\n"
#           f"Peshin: {js['vaqtlar']['peshin']}\n"
#           f"Asr: {js['vaqtlar']['asr']}\n"
#           f"Shom: {js['vaqtlar']['shom']}\n"
#           f"Xufton: {js['vaqtlar']['xufton']}\n")
# else:
#     print("Noma'lum xatolik yuzaga keldi!")
#
