def count_run_wic(balling_Status):
    run = 0
    wick = 0
    over = 0
    over_ball = 0
    for i in range(len(balling_Status)):
        if balling_Status[i] == 'W':
            wick += 1
        else:
            run = int(balling_Status[i]) + run
        over_ball += 1
        if over_ball == 6:
            over += 1
            over_ball = 0

    if over>=1 and over_ball!=0 :
        print(f"{over}.{over_ball} overs",end=' ')
    else:
        print(f"{over}.{over_ball} over", end=' ')
    if run>1:
        print(f'{run} Runs',end=' ')
    else:
        print(f'{run} Run', end=' ')
    if wick>1:
        print(f"{wick} Wickets",end=" ")
    else:
        print(f"{wick} Wicket", end=" ")
    print()
for i in range(int(input())):
    ball=input().strip()
    count_run_wic(ball)
