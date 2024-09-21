import random

# ฟังก์ชันสำหรับแสดงจำนวนเต็มบวก 4 จำนวน ในช่วง 1 ถึง 5 สำหรับผู้เข้าแข่งขันหมายเลข i
def generate_competitor_scores(num_competitors):
    max_total_score = 0  # ตัวแปรสำหรับเก็บคะแนนรวมสูงสุด
    max_competitor = 0  # ตัวแปรสำหรับเก็บหมายเลขผู้เข้าแข่งขันที่มีคะแนนสูงสุด

    for i in range(1, num_competitors + 1):
        # สร้างจำนวนเต็ม 4 จำนวน อยู่ในช่วง 1 ถึง 5
        scores = [random.randint(1, 5) for _ in range(4)]
        total_score = sum(scores)  # คำนวณผลรวมคะแนน

        print(f'ผู้เข้าแข่งขันหมายเลข {i}: {scores} (ผลรวม: {total_score})')

        # ตรวจสอบว่าคะแนนรวมนี้สูงกว่าคะแนนสูงสุดก่อนหน้าไหม
        if total_score > max_total_score:
            max_total_score = total_score
            max_competitor = i

    # แสดงผลผู้เข้าแข่งขันที่ได้คะแนนรวมสูงสุด
    print(f'\nผู้เข้าแข่งขันหมายเลข {max_competitor} ได้ผลรวมคะแนนสูงสุด: {max_total_score}')

# กำหนดจำนวนผู้เข้าแข่งขัน
num_competitors = 5  # ตัวอย่างกำหนดเป็น 5 คน
generate_competitor_scores(num_competitors)
