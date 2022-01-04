from Scheduler import *
import User
import random
import datetime
from datetime import date
import csv


if __name__ == "__main__":
    """
    Output Results:Initialise User
    Students and Researchers
    """
    user_names = ["s1", "s2", "s3", "s4", "s5", "s6", "s7", "s8", "s9", "s10", "s11", "s12", "s13", "s14", "s15",
                  "r1", "r2", "r3", "r4", "r5", "r6", "r7", "r8", "r9", "r10"]
    user_types = ["student", "student", "student", "student", "student", "student", "student", "student",
                  "student", "student", "student", "student", "student", "student", "student", "researcher",
                  "researcher", "researcher", "researcher", "researcher", "researcher", "researcher",
                  "researcher", "researcher", "researcher"]
    users = []
    requests = []
    requests2 = []
    scheduler = Scheduler()
    for i in range(len(user_names)):
        users.append(User.User(user_names[i], user_types[i]))
    n = 0
    """
    The number of jobs processed in each queue per week;
    """
    now_time = datetime.datetime.now()
    now_time = datetime.datetime.now() - datetime.timedelta(hours=now_time.hour, minutes=now_time.minute,
        seconds = now_time.second, microseconds=now_time.microsecond) + datetime.timedelta(hours=now_time.hour +1)
    week_one = dict()
    week_one["short"] = 0
    week_one["medium"] = 0
    week_one["large"] = 0
    week_one["gpu"] = 0
    week_one["huge"] = 0
    week_two = dict()
    week_two["short"] = 0
    week_two["medium"] = 0
    week_two["large"] = 0
    week_two["gpu"] = 0
    week_two["huge"] = 0
    week_three = dict()
    week_three["short"] = 0
    week_three["medium"] = 0
    week_three["large"] = 0
    week_three["gpu"] = 0
    week_three["huge"] = 0
    week_four = dict()
    week_four["short"] = 0
    week_four["medium"] = 0
    week_four["large"] = 0
    week_four["gpu"] = 0
    week_four["huge"] = 0
    week_five = dict()
    week_five["short"] = 0
    week_five["medium"] = 0
    week_five["large"] = 0
    week_five["gpu"] = 0
    week_five["huge"] = 0
    for user in users:
        for i in range(10):
            n = n + 1
            r = random.randint(0,100)
            """
            short type 45%
            medium type 30%
            large  type 10%
            gpu type 10 %
            huge type 5%
            """
            if 1 <= r <45:
                time = 0.5 if random.random() < 0.75 else 1
                nodes = 2 if random.random() < 0.75 else 1
                req = user.create_request("request " + str(n) + " short", nodes, time, "short")
                if req.title != "Insufficient balance":
                    requests.append(req)
            if 45 <=r < 75:
                time = None
                time_r = random.random()
                if time_r < 0.1:
                    time = 3
                elif time_r < 0.25:
                    time = 4
                elif time_r < 0.5:
                    time = 5
                elif time_r < 0.75:
                    time = 6
                elif time_r < 0.9:
                    time = 7
                else:
                    time = 8
                nodes = random.randint(1, 6) + random.randint(1, 6)
                req = user.create_request("request "+str(n)+" medium", nodes, time, "medium")
                if req.title != "Insufficient balance":
                    requests.append(req)
            if 75 <= r < 85:
                time = 8 + random.randint(0, 4) + random.randint(0, 4)
                nodes = random.randint(1, 32) + random.randint(1, 32)
                req = user.create_request("request " + str(n) + " large", nodes, time, "large")
                if req.title != "Insufficient balance":
                    requests.append(req)
            if 85 <=r <95:
                time = random.randint(1, 16)
                nodes = random.randint(1,8)
                req = user.create_request("request " + str(n) + " gpu", nodes, time, "gpu")
                if req.title != "Insufficient balance":
                    requests.append(req)
            if 95 <= r <= 100 :
                nodes = None
                time = None
                if random.random() < 0.5:
                    nodes = 64 + random.randint(1, 32) + random.randint(1, 32)
                    time = random.randint(1, 24)
                else:
                    nodes = random.randint(1, 32) + random.randint(1, 32)
                    time = 24 + random.randint(1, 24)
                req = user.create_request("request " + str(n) + " huge", nodes, time, "huge")
                if req.title != "Insufficient balance":
                    requests.append(req)

    for req in requests:
        scheduler.add_request(req)
    """
    Simulation start time
    :param time_start: datetime
    """
    time_start = scheduler.actual_time
    scheduler.schedule()
    output_file = open("C:\\Users\\ulysses\\PycharmProjects\\RASD_SQTA\\outputresults.csv", 'w+', newline="")
    writer = csv.writer(output_file)
    """
    Hourly node consumption price: 6 pence
    Hourly node consumption price(with gpu): 6.6 pence
    """
    writer.writerow(["user name", "request number", "time round ratio", "waiting_time",
                     "running_time", "node_hour", "request_cost", "request_type", "end"])
    """
        Simulation end time
        :param max_end_time: datetime
    """
    max_end_time = scheduler.actual_time
    for index, req in enumerate(requests):
        username = req.user.user_name
        request_number = index
        node_hour = (req.req_time.days * 24 + req.req_time.seconds / 3600) * req.nbr_nodes
        if req.req_type == "gpu":
            request_cost = node_hour * 6.6
        else:
            request_cost = node_hour * 6
        request_running_start_time = req.time_of_computation
        waiting_time = req.time_of_computation - time_start
        running_time = req.req_time
        end_time = request_running_start_time + running_time
        if end_time > max_end_time:
            max_end_time = end_time
        writer.writerow([username, request_number, (waiting_time.days*24 + waiting_time.seconds/3600 +running_time.days*24 +running_time.seconds/3600)/(running_time.days*24 +
                                                    running_time.seconds/3600), waiting_time,
                         running_time, node_hour, request_cost, req.req_type, end_time])
        i = date.isocalendar(end_time)[1]
        if i == 1:
            week_one[req.req_type] = 1 + week_one[req.req_type]
        elif i == 2:
            week_two[req.req_type] = 1 + week_two[req.req_type]
        elif i == 3:
            week_three[req.req_type] = 1 + week_three[req.req_type]
        elif i == 4:
            week_four[req.req_type] = 1 + week_four[req.req_type]
        elif i == 5:
            week_five[req.req_type] = 1 + week_five[req.req_type]
    writer.writerow([week_one])
    print("week_one")
    print(week_one)
    print("week_two")
    print(week_two)
    writer.writerow([week_two])
    print("week_three")
    print(week_three)
    writer.writerow([week_three])
    print("week_four")
    print(week_four)
    writer.writerow([week_four])
    print("week_five")
    print(week_five)
    writer.writerow([week_five])
    print("Simulation start time")
    print(time_start)
    print("total available node hour without gpu")
    print(((max_end_time - time_start).seconds/3600 + (max_end_time - time_start).days*24)*120)
    print("total available node hour with gpu")
    print(((max_end_time - time_start).seconds/3600 + (max_end_time - time_start).days*24)*8)
    print("Simulation end time")
    print(max_end_time)







