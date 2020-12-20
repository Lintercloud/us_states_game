from turtle import *
import pandas
from states_board import State_board
def get_mouse_click_coor(x, y):
    print(x, y)

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)   #增加新圖片為shape
shape(image)

state_office = State_board()
state_office_point = State_board()
state_office_point.update_point()   #為了讓分數一開始就出現
answer_list = []
miss_state = []  #用來紀錄沒猜到的州
data = pandas.read_csv("50_states.csv")
data_list = data.state.to_list()    #將資料轉成list 必須用series
print(data_list)

while len(answer_list) < 50:
    answer = screen.textinput(title="Guess the States", prompt="What's your next guess").title() #
    if answer == "Q":
        for state in data_list:
            if state not in answer_list:
                miss_state.append(state)
        new_data = pandas.DataFrame(miss_state)           #創造檔案，紀錄
        new_data.to_csv("states_to_learn.csv")
        break
    if any(data["state"].str.contains(answer)):            #假如猜的州有在資料名單中
        if answer not in answer_list:                      #假如名單已經猜過了
            answer_list.append(answer)
            new_x = int(data.x[data.state == answer])
            new_y = int(data.y[data.state == answer])
            state_office.show_state(new_x, new_y, answer)
            state_office_point.get_point()
        elif answer in answer_list:
            print("you have guess it")
            continue


