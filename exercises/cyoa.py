"""Formula One create your own adventure game."""

__author__ = "730609760"

from random import randint
from random import uniform

BARF: str = "\U0001F92E"
player: str
points: int
dreaming: bool
choose_to_call: bool


def greet() -> None:
    """Greets the player and gives game context."""
    global player
    player = input("What is your name? ")

    print("\n")
    print(f"Hello {player}, and welcome to this Formula One stragety role play game!")
    print("Throughout this game, you will be faced with many different choices that affects how your adventure plays out.")
    print("You are dreaming that you are a UNC freshman enrolled in Comp 110 (exciting stuff)!")
    print("\n")
    print("type-type-type...munch-munch-munch...type-type-munch...")
    print("It's precisely 7:43pm on October 5th (in your dream of course).")
    print("You are eating dinner at Lenior dining hall while working on Comp 110.")
    print("Despite the gracious due date extention from Professor Jordan, you are just starting EX06")
    print("and the sweet potatos that you are trying to eat are not doing much for your creativity.")
    print("Searching for some inspiration you glance around the room and your eyes settle on the TV.")
    print("Thats when you see it. BREAKING NEWS: Scuderia Ferrari sacks entire stragety team after")
    print("multiple, dismal performances. Urgently hiring anyone who completes half a semester of")
    print("Comp 110.")
    print(f"{player}: 'Hey, I have completed half a semester of Comp 110!' you exclaim. 'If I get a job with")
    print("Scuderia Ferrari I won't have to eat these wretched sweet potatos anymore!'")
    print("\n")


def wake() -> bool:
    """Play is face with a choice to wake up from their dream."""
    sweet_potatos_points()
    global player
    wake: str = input(f"{player}, would you like to wake from your dream? y/n: ")
    answered: bool = False
    while not answered:
        if wake == "y":
            answered = True
            print("As you wish, but first you must finish your sweet potatos. MWAAA-HAAA-HAAAAA!!!")
            print("\n")
            global points
            points += 1
            end()
            return False
        elif wake == "n":
            print("\n")
            answered = True
            return True
        else:
            wake = input("Invalid answer, please try again. y/n: ")
    return True
    

def call_choice() -> None:
    """Player is faced with a choice to ask for a job."""
    call_decision: str = input("Would you like call Scuderia Ferrari and ask for a job, \nor will you suffer four years of eating Top of Lenior sweet potatos? call/sweet potatos: ")
    answered: bool = False
    while not answered:
        if call_decision == "sweet potatos":
            print("\n")
            answered = True
            sweet_potatos()
        elif call_decision == "call":
            print("\n")
            answered = True
            global choose_to_call
            choose_to_call = True
            call_ferrari()
        else:
            call_decision = input("Invalid answer, please try again. call/sweet potatoes: ")


def sweet_potatos() -> None:
    """Player chooses to eat sweet potatos."""
    global points
    points += randint(1, 10000000000)
    print(f"Over your next four years at UNC, you will suffer through eating {points} Top of Lenior sweet potatos.")
    print(BARF)
    print("\n")
    wake()
    

def call_ferrari() -> None:
    """Role-plays calling Scuderia Ferrari to ask for a job."""
    global player
    print("Motivated by the thought of no longer eating Top of Lenior sweet potatos,")
    print("you pick up your phone and call the Scuderia Ferrari recruiting hotline.")
    print("RING-RING...RING-RING...RING-RING...")
    print("Recruiter: 'Hello, you have reached the Scuderia Ferrari recruiting")
    print("office, how may I help you?'")
    print(f"{player}: 'Hello, my name is {player} and I would like a job as a strategist.'")
    print(f"Recruiter: 'Copy that {player}, do you have half of a semester of experience in Comp 110?'")
    print(f"{player}: 'Yes.'")
    print("Recruiter: Copy, we will call back with a job offer.'")
    print("Click...")
    print("\n")
    wake()


def job_offer(min: int, sweet_potatos_eaten: int) -> int:
    """The player is faced with the decision to take a job or not."""
    global player
    """Player enter job offer negotiations."""
    ferrari_offer: int = randint(50000, 100000)
    print("RING-RING...RING-RING...RING-RING...")
    print(f"Recruiter: 'Hello again {player}, you have to answer a few questions")
    print("before we can offer you a job.'")
    print(f"{player}: 'Okay, let's get started then!'")
    print("Recruiter: Have you every eaten Top of Lenior sweet potatos?")
    if sweet_potatos_eaten > 0:
        print(f"{player}: 'Yes, I have eaten {sweet_potatos_eaten} Top of Lenior sweet potatos.'")
    else:
        print(f"{player}: 'No, I have eaten {sweet_potatos_eaten} Top of Lenior sweet potatos.'")
        print(f"Recruiter: 'Unfortunately we cannot offer you a job if you have eaten {sweet_potatos_eaten}")
        print("Top of Lenior sweet potatoes.")
        eat_sweet_potatoes: str = input("Recruiter: 'Will you eat 1 Top of Lenior sweet potato to be eligable for a job offer?' y/n: ")
        answered: bool = False
        while not answered:
            if eat_sweet_potatoes == "n":
                answered = True
                print("Recruiter: 'Sorry, but we are unable to offer you a job at this time.")
                end()
                return sweet_potatos_eaten
            elif eat_sweet_potatoes == "y":
                answered = True
                print(BARF)
                print("Recruiter: 'Congrats on eating a Top of Lenior sweet potato! Now you are eligable for a job offer!'")
                sweet_potatos_eaten += 1
            else:
                eat_sweet_potatoes = input("Invalid answer, please try again. y/n: ")
    print(f"Recruiter: 'Based on your stellar credentials we can offer you a salary of ${ferrari_offer} per year'")
    if min < ferrari_offer:
        print(f"{player}: 'I accept your offer! I cannot wait to start!'")
        return sweet_potatos_eaten
    elif min == ferrari_offer:
        print(f"{player}: 'I accept your offer! I cannot wait to start!'")
        return sweet_potatos_eaten
    else:
        print(f"{player}: 'That is below the minimum salary I will work for. I cannot accept this offer.'")
        print(f"Recruiter: 'Copy. We could offer you ${ferrari_offer + 100000} if you eat another Top of Lenior sweet potato.")
        counter_offer: str = input(f"Do you accept this new offer of ${ferrari_offer + 100000}? y/n:")
        answered = False
        while not answered:
            if counter_offer == "y":
                answered = True
                print(f"{player}: 'I accept your offer! I cannot wait to start!'")
                sweet_potatos_eaten += 1
                wake()
                return sweet_potatos_eaten
            elif counter_offer == "n":
                answered = True
                print("Recruiter: 'Sorry, but we are unable to offer you a job at this time.")
                end()
            else: 
                counter_offer = input("Invalid answer, please try again. y/n: ")
    print("\n")
    wake()
    return sweet_potatos_eaten


def qualifying_sim() -> None:
    """Play fulfills their role as a strategist."""
    Driver = tuple[str, float, float, float, float, float, float, float, float, float, float, float]
    ver: Driver = ("Ver", 96.0, 73.0, 99.0, 84.0, 98.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    ham: Driver = ("Ham", 94.0, 94.0, 96.0, 91.0, 93.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    lec: Driver = ("Lec", 92.0, 67.0, 96.0, 85.0, 94.0, 100.0, 100.0, 100.0, 100.0, 100.0, 25.0)
    rus: Driver = ("Rus", 91.0, 66.0, 94.0, 83.0, 94.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    alo: Driver = ("Alo", 90.0, 99.0, 90.0, 76.0, 90.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    nor: Driver = ("Nor", 90.0, 66.0, 94.0, 77.0, 92.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    sai: Driver = ("Sai", 89.0, 73.0, 92.0, 80.0, 90.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    per: Driver = ("Per", 87.0, 84.0, 93.0, 85.0, 84.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    vet: Driver = ("Vet", 85.0, 93.0, 89.0, 80.0, 83.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    gas: Driver = ("Gas", 83.0, 64.0, 88.0, 76.0, 83.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    bot: Driver = ("Bot", 83.0, 78.0, 84.0, 90.0, 83.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    alb: Driver = ("Alb", 82.0, 61.0, 80.0, 76.0, 87.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    ric: Driver = ("Ric", 82.0, 83.0, 84.0, 84.0, 81.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    oco: Driver = ("Oco", 82.0, 64.0, 88.0, 76.0, 82.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    mag: Driver = ("Mag", 80.0, 70.0, 82.0, 78.0, 81.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    lan: Driver = ("Str", 80.0, 66.0, 88.0, 75.0, 78.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    msc: Driver = ("Msc", 80.0, 59.0, 83.0, 82.0, 80.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    zho: Driver = ("Zho", 78.0, 52.0, 82.0, 73.0, 80.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    tsu: Driver = ("Tsu", 77.0, 58.0, 77.0, 74.0, 79.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    lat: Driver = ("Lat", 67.0, 62.0, 72.0, 74.0, 65.0, 100.0, 100.0, 100.0, 100.0, 100.0, 95.0)
    drivers: list[Driver] = [ver, ham, rus, alo, nor, sai, per, vet, gas, bot, alb, ric, oco, mag, lan, msc, zho, tsu, lat]
    print("Your first assignment will be the Japanese Grand Prix in Suzuka.")
    print("You will be the cheif strategist for Ferrari driver, Charles Leclerc.")
    print("Leclerc will be relying on you guide him to a successful qualifying position.")
    print("As the cheif strategist, it is up to you to determine when Leclerc should leave")
    print("the pit box, what tyres to use, and how to warm up the tyres.")
    print("Qualifying is split into three sessions: Q1, Q2, and Q3.")
    print("In order to advance into the next round, Leclerc must be in the top 15 for Q1, and the top 10 for Q2.")
    print("Q3 will decide the starting order for the Grand Prix the following day.")
    print("The timing screen will be displayed on the right side of your screen, and it will tell you the")
    print("drivers who are still currently in qualifying.")
    print("Leclerc's qualifying time will be determined based off of his stats, tyre condition, and tyre tempature.")
    print("It is your job to find the optimal balance between tyre tempature and tyre condition.")
    print("If the tyre temperature is too low, Leclerc will not have enough grip, but reaching a")
    print("higher the tyre temperature worsens the condition of the tyre.")
    print("Given that all of the other driver have experienced strategists, they will be using an ideal strategy, but")
    print("you will have to find the ideal strategy yourself. Good luck!")
    print("\n")
    i: int = 0
    t: int = 6
    lec_qualified: bool = True
    drivers_quali_name: list[str]
    drivers_quali_time: list[float]
    c: float
    confidence: float
    stat_item: float
    stat_tyre_item: float
    stat_temp_item: float
    increase_temp: float
    tyre_temp: float
    stat: float
    stat_tyre: float
    lec_time: float
    time: float
    i_check: int
    time_i: int
    checking_i: int
    drivers_i: int
    while i < 3 and lec_qualified:
        drivers_quali_name = []
        drivers_quali_time = []
        c = uniform(1, 30)
        confidence = 1.1 + (c / 1000)
        print(f"The current session is Q{i + 1}")
        print(f"Current tyre temperature is {lec[11]}% of maximum.")
        print(f"Current tyre condition is {lec[t]}% of maximum.")
        print("\n")
        wake()
        increase_temp = float(input("What percentage would you like Leclerc to increase the tyre temperature by? Enter a float: "))
        print("\n")
        tyre_temp = lec[11] + increase_temp
        stat = lec[1]
        stat_tyre = lec[6]
        lec_time = ((133.47 - (i * .75)) * (1 + ((tyre_temp - stat) / (2 * (stat_tyre) - tyre_temp)))) * confidence
        drivers_quali_name.append(lec[0])
        drivers_quali_time.append(lec_time)
        for item in drivers:
            stat_item = item[1]
            stat_tyre_item = item[6]
            stat_temp_item = item[11]
            time = ((133.47 - (i * .75)) * (1 + ((stat_temp_item - stat_item) / (2 * (stat_tyre_item)) - stat_temp_item))) * confidence
            drivers_quali_name.append(item[0])
            drivers_quali_time.append(time)

        i_check = 0
        while i_check < 5 and i < 2:
            time_i = 0
            checking_i = 0
            while checking_i < len(drivers) and time_i < len(drivers):
                if drivers_quali_time[time_i] < drivers_quali_time[checking_i]:
                    time_i += 1
                elif drivers_quali_time[time_i] == drivers_quali_time[checking_i]:
                    checking_i += 1
                else:
                    checking_i += 1
            drivers_quali_name.pop(time_i)
            drivers_quali_time.pop(time_i)
            drivers.pop(time_i)
            i_check += 1

        drivers_i = 0
        while drivers_i < len(drivers_quali_name):
            print(f"{drivers_quali_name[drivers_i]}: {drivers_quali_time[drivers_i]}")
            drivers_i += 1

        i += 1
        t += 1
    global dreaming
    dreaming = False
    end()
          

def sweet_potatos_points() -> None:
    """Updates the player on how many sweet potatos they have eaten."""
    global points
    if points != 1:
        print(f"You have eaten {points} sweet potatos so far!")
        print("\n")
    else:
        print(f"You have eaten {points} sweet potato so far!")
        print("\n")


def end() -> None:
    """Game ending point."""
    global dreaming
    if points > 0:
        print("You are abruptly awaken from your nightmare, and you feel as if you have")
        print(f"just eaten {points} servings of Top of Lenior sweet potatos.")
        print(BARF)
        print("Oh you poor thing. You best go use some mouthwash.")
        dreaming = False
    else:
        print("You are awaken from a wonderful night sleep and are looking forward to")
        print("a delicous breakfast at the Top of Lenior.")
        print(f"For some strange reason you can distinclty remember eating {points} servings of")
        print("Top of Lenior sweet potatos. What a pleasant dream you must have had.")
        dreaming = False


def main() -> None:
    """Game entry point."""
    global player
    global points 
    points = 0
    global dreaming
    dreaming = True
    global choose_to_call
    choose_to_call = False
    greet()
    while dreaming:
        wake()
        while not choose_to_call and dreaming:
            call_choice()
            sweet_potatos_points()
        while dreaming:
            print("Given that you are an ace student, and you have been taught by the legendary")
            print("Professor Jordan, you decide that you will only accept the job with Scuderia Ferrari")
            print("if it is above the minimum salary you have in mind. What is the minimum salary that you will accept?")
            print("\n")
            mimimum_salary: int = 75000
            print(f"{player}: 'The minimum salary I will accept is ${mimimum_salary}.'")
            print("\n")
            points = job_offer(mimimum_salary, points)
            while dreaming:
                print(f"Congrats, you signed with Scuderia Ferrari and only had to eat {points} top of Lenior sweet potatos!")
                print("\n")
                sweet_potatos_points
                qualifying_sim()
            dreaming = False


if __name__ == "__main__":
    main()