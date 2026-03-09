# Count number of digit with duplicate

# =============================================================================
# 1234
# 2344
# 
# set(str(1234))
# set(str(2344))
# 
# count = 0
# 
# for num in range(1000, 10000):
#     if len(set(str(num))) != len(str(num)):
#         count += 1
#         
# 
# print(count)
# -----------------------------
# =============================================================================

# Count permutations of Pencil start with P or contains Pen

# =============================================================================
# from itertools import permutations
# 
# pencil_p = permutations('pencil')
# print(list(pencil_p))
# 
# pencil_p = permutations('pencil')
# count = 0
# for per in pencil_p:
#     if per[0] == 'p': # per.startswith('p')
#         count += 1
#         
# print(count)
# -----------------------------------
# pencil_p = permutations('pencil')
# for per in pencil_p:
#     per_join = ''.join(per)
#     print(per_join)
# -----------------------------------
#  
# pencil_p = permutations('pencil')
# count = 0
# 
# for per in pencil_p:
#     per_join = ''.join(per)
#     if 'pen' in per_join:
#         count += 1
#         
# print(count)
# ----------------------------------
# =============================================================================

# Count permutations of 4 players

# =============================================================================
# from itertools import permutations
# 
# prize = 0
# for per in permutations([1, 2, 3, 4]):
#     for q_id, p_id in enumerate(per, start=1):
#         if q_id == p_id:
#             prize += 1
#             
# print(prize)
# ------------------------------------
# =============================================================================

# Count permutations of 2 oranges and 2 pears

# =============================================================================
# --------------------------------------
# =============================================================================

# Count permutation of 3 boys and 6 girls doesn't contain 2 boys beside

# =============================================================================
# from itertools import permutations
# 
# string = 'BBBGGGGGG'
# total = 0
# for per in permutations(string):
#     is_valid = 1
#     for i in range(len(per)-1):
#         if per[i] == per[i + 1] == 'B':
#             is_valid = 0
#             break
#     total += is_valid
#     
# print(total)
# =============================================================================

# =============================================================================
# # از کتابخونه itertools تابع permutations رو import می کنیم
# from itertools import permutations
# 
# # تابع solve_yasuj رو تغریف می کنیم
# def solve_yasuj():
#     # رشته اولیه yasuj
#     word = 'yasuj'
#     # تمام جایگشت های رشته رو به صورت لیست رشته ها تولید می کنیم
#     all_permutations = [''.join(per) for per in permutations(word)]
#     
#     # ایجاد یه لیست خالی برای ذخیره جایگشت های حالت شرط:
#         # حرف اول از نظر الفبایی از نظر الفبایی از حرف آخر زودتر اومده باشه
#         valid_permutations = []
#         
#         #پیمایش تمام جایگشت ها
#         for per in all_permutations:
#             # چک کردن زودتر اومدن حرف اول از حرف آخر
#             if per[0] < per[-1]:
#                 # اضافه کردن جایگشت به لیست معتبر
#                 valid_permutations.append(per)
#                 
#                 # چاپ تعداد جایگشت های معتبر
#         print(len(valid_permutations))
# 
# # چاپ لیست جایگشت های معتبر
#         print(valid_permutations)
# 
# # اجرای مستقیم تابع
# if __name__ == "__main__":
#     solve_yasuj()
# 
# =============================================================================

# کتابخونه تولید اعداد تصادفی
import random

# تابع اصلی حل مساله
def solve_experiment():
    
    # لیست نوشته های 100 نفر
    all_people_numbers = []
    
    #تعداد افراد
    num_people = 100
    
    # هر نفر چند عدد میتونه بنویسه
    numbers_per_person = 5
    
    # حلقه برای 100 نفر
    for _ in range(num_people):
        
        # لیست اعداد یک نفر
        person_numbers = []
        
        # هر نفر 5 عدد وارد می کنه
        for _ in range(numbers_per_person):
            
            # تولید اعداد تصادفی بین 0 و 1
            r = random.random()
            
            # اگر کمتر از 0.6 باشه اعداد از 1 تا 4 انتخاب میشه
            if r < 0.6:
                num = random.randint(1, 4)
                
                # در غیر این صورت عدد 5 انتخاب میشه
            else:
                num = 5
                
                # اضافه کردن عدد به لیست شخص
            person_numbers.append(num)
            
        # افزودن لیست شخص به لیست کل نوشته های افراد
        all_people_numbers.append(person_numbers)
        
    # محاسبه مجموع همه اعداد
    total_sum = sum(sum(person) for person in all_people_numbers)
    
    # تعداد کل اعداد نوشته شده
    total_count = num_people * numbers_per_person
    
    # محاسبه میانگین
    average = total_sum / total_count
    
    # چاپ میانگین
    print(average)
    
    # چاپ لیست نتایج
    print(all_people_numbers)
    
    
solve_experiment()
