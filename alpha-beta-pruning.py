import random

def Generate_Points():
    # return [random.randint(10, 120) for _ in range(8)]
    lst=[]
    for i in range(8):
        lst.append(random.randint(10,130))
    return lst

def alpha_beta_pruning(points, alpha, beta):
    if not points:
        return 0

    max_value = float('-inf')

    for value in points:
        max_value = max(max_value, -alpha_beta_pruning(points[1:], -beta, -alpha) + value)
        alpha = max(alpha, max_value)
        if alpha >= beta:
            break

    return max_value

student_id = input("Enter your student ID: ")
total_points_to_win = int(input("Enter the total points to win: "))  # Take total_points_to_win as input
random_points = Generate_Points()

print(f"Generated 8 random points between the minimum and maximum point limits: {random_points}")

achieved_point = alpha_beta_pruning(random_points, float('-inf'), float('inf'))

print(f"Total points to win: {total_points_to_win}")
if achieved_point >= total_points_to_win:
    winner = "Optimus Prime"
else:
    winner = "Megatron"
print(f"achieved points= {achieved_point}")
print(f"The winner is {winner}")
