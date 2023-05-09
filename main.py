from datetime import datetime
from student import students, student_cgpa

# Data types
# name = "Dami" #str
# total_sales = 90 #int 
# amount = 12.99 #float
# is_live = True #bool

# function
def say_hello(name):
    print(f"Hello {name}")
    return 


# def project_status(project_name,is_live):
#     # if is_live:
#     #     print(f"Congratulations.... Project {project_name} is LIVE!!!!")
#     # else:
#     #     print("There is more work to be done")

#     # Match case only works for python v3.10 and higher 
#     match is_live:
#         case True:
#             print(f"Congratulations.... Project {project_name} is LIVE!!!!")
#         case False:
#             print("There is more work to be done")





if __name__ == "__main__":
    # say_hello("Dami")
    # project_status("ODT Channel", True)

    # Tuple 
    my_tuple = ("Rice","Beans","Chicken")

    # for food in my_tuple:
    #     print(food)

    # A List
    football_team = ["Man-U", "Chelsea", "PSG", "Liverpool"]

    # total_teams = len(football_team)

    # print("total_teams ->", total_teams)

    # first_two = football_team[:2]

    # print("first_two ->", first_two)

    last_two = football_team[2:]

    # print("last_two ->", last_two)



    # for team in football_team:
    #     print(f"Team Name: {team}")


    # Dictionary 
    scores = {
        "teams": football_team,
        "points": [1, 2, 3, 4]
    }

    # team_points = scores.get("points")
    # print("team_points", team_points)
    # teams = scores["teams"]
    # print("teams", teams)

    # print("all keys", scores.keys())
    
    # print("all values", scores.values())

    # print(datetime.now())

    # print("students ->", students)

    cgpa = student_cgpa(students)
    print("cgpa ", cgpa)