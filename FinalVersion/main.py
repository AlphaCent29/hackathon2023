from kivy.core.window import Window
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.navigationdrawer import MDNavigationLayout
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screenmanager import ScreenManager
from kivymd.uix.screen import Screen


Window.size = (480, 853)

MainPage = '''
<DrawerClickableItem@MDNavigationDrawerItem>
    #focus_color: "#000000"
    text_color: "#000000"
    icon_color: "#000000"
    ripple_color: "#6e6e6e"
    ripple_alpha: 0.1
    selected_color: "#827ad3"


<DrawerLabelItem@MDNavigationDrawerItem>
    text_color: "#000000"
    icon_color: "#000000"
    focus_behavior: False
    selected_color: "#000000"
    _no_ripple_effect: True


MDScreen:

    MDNavigationLayout:

        MDScreenManager:
            id:manager

            
            MDScreen:      #Экран календаря
                name: 'calendar'
                md_bg_color: "#827ad3"
                FloatLayout:
                    Button:       #кнопка добавить задачу
                        background_disabled_normal: 'images\plus1.png'
                        background_normal: 'images\plus1.png'
                        background_down: 'images\plus1.png'
                        text: ' '
                        pos_hint: {'center_x': 0.5, 'center_y': 0.08}
                        size_hint: 0.23, 0.14
            
                        on_press:
            
            
                    Button:       #кнопка календаря
                        background_disabled_normal: 'images\calendar1.png'
                        background_normal: 'images\calendar1.png'
                        background_down: 'images\calendar1.png'
                        text: ' '
                        pos_hint: {'center_x': 0.5, 'center_y': 0.75}
                        size_hint: 0.57, 0.35
            
                    BoxLayout:   #общий контейнер со всеми задачами
                        size_hint: 0.97, 0.45
                        pos_hint: {'center_x': 0.5, 'center_y': 0.35}
                        orientation:'vertical'
                        padding: 0, 25, 0, 25
                        spacing: 25
                        BoxLayout:    #контейнер задачи и чекбокса
                            size_hint: 0.85, 0.85
                            pos_hint: {'center_x':0.5, 'center_y':0.5}
                            spacing: 15
                            BoxLayout:    #контейнер задачи
                                size_hint: 0.95, 0.95
                                pos_hint: {'center_x':0.5, 'center_y':0.5}
                                canvas.before:
                                    Color:
                                        rgba: 1, 0.86, 0.52, 1
                                    Line:
                                        width: 10
                                        rectangle: self.x, self.y, self.width, self.height
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                                Label:
                                    pos_hint: {'center_x':0.3, 'center_y':0.5}
                                    text:'Сделать домашку'
                            BoxLayout:     #котейнер с чекбоксом
                                size_hint: 0.1, 0.1
                                pos_hint: {'center_x':0.95, 'center_y':0.5}
                                CheckBox:
                                    id: check
                                    width: 35
                                    size: [35, 35]
                                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                                    on_release:
            
            
                        BoxLayout:    #контейнер задачи и чекбокса
                            size_hint: 0.85, 0.85
                            pos_hint: {'center_x':0.5, 'center_y':0.5}
                            spacing: 15
                            BoxLayout:    #контейнер задачи
                                size_hint: 0.95, 0.95
                                pos_hint: {'center_x':0.5, 'center_y':0.5}
                                canvas.before:
                                    Color:
                                        rgba: 1, 0.86, 0.52, 1
                                    Line:
                                        width: 10
                                        rectangle: self.x, self.y, self.width, self.height
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                                Label:
                                    pos_hint: {'center_x':0.3, 'center_y':0.5}
                                    text:'Сделать домашку'
                            BoxLayout:     #котейнер с чекбоксом
                                size_hint: 0.1, 0.1
                                pos_hint: {'center_x':0.95, 'center_y':0.5}
                                CheckBox:
                                    id: check
                                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                                    on_release:
            
            
                        BoxLayout:    #контейнер задачи и чекбокса
                            size_hint: 0.85, 0.85
                            pos_hint: {'center_x':0.5, 'center_y':0.5}
                            spacing: 15
                            BoxLayout:    #контейнер задачи
                                size_hint: 0.95, 0.95
                                pos_hint: {'center_x':0.5, 'center_y':0.5}
                                canvas.before:
                                    Color:
                                        rgba: 1, 0.86, 0.52, 1
                                    Line:
                                        width: 10
                                        rectangle: self.x, self.y, self.width, self.height
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                                Label:
                                    pos_hint: {'center_x':0.3, 'center_y':0.5}
                                    text:'Сделать домашку'
                            BoxLayout:     #котейнер с чекбоксом
                                size_hint: 0.1, 0.1
                                pos_hint: {'center_x':0.95, 'center_y':0.5}
                                CheckBox:
                                    id: check
                                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                                    on_release:
            
            
                        BoxLayout:    #контейнер задачи и чекбокса
                            size_hint: 0.85, 0.85
                            pos_hint: {'center_x':0.5, 'center_y':0.5}
                            spacing: 15
                            BoxLayout:    #контейнер задачи
                                size_hint: 0.95, 0.95
                                pos_hint: {'center_x':0.5, 'center_y':0.5}
                                canvas.before:
                                    Color:
                                        rgba: 1, 0.86, 0.52, 1
                                    Line:
                                        width: 10
                                        rectangle: self.x, self.y, self.width, self.height
                                    Rectangle:
                                        pos: self.pos
                                        size: self.size
                                Label:
                                    pos_hint: {'center_x':0.3, 'center_y':0.5}
                                    text:'Сделать домашку'
                            BoxLayout:     #котейнер с чекбоксом
                                size_hint: 0.1, 0.1
                                pos_hint: {'center_x':0.95, 'center_y':0.5}
                                CheckBox:
                                    id: check
                                    pos_hint: {'center_x':0.5, 'center_y':0.5}
                
                
                MDTopAppBar:
                    title: "Главная"
                    elevation: 3
                    pos_hint: {"top": 1}
                    md_bg_color: "#ffdb84"
                    specific_text_color: "#000000"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]
                    
            MDScreen:     #Основная странциа
                name: 'home'
                md_bg_color: "#827ad3"
                FloatLayout:
                    Label:
                        text: 'Hello world'
                        pos_hint:{'center_x':0.5, 'center_y':0.5}
                MDTopAppBar:    #Топ бар с кнопкой меню
                    title: "Главная"
                    elevation: 3
                    pos_hint: {"top": 1}
                    md_bg_color: "#ffdb84"
                    specific_text_color: "#000000"
                    left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]


        MDNavigationDrawer:    #Навигационное меню
            id: nav_drawer
            radius: (0, 16, 16, 0)

            MDNavigationDrawerMenu:

                MDNavigationDrawerHeader:
                    title: "Step by step"
                    title_color: "#4a4939"
                    text: "Just do it"
                    spacing: "4dp"
                    padding: "12dp", 0, 0, "56dp"

                MDNavigationDrawerLabel:
                    text: "Меню"
                    
                DrawerClickableItem:
                    icon: "home"
                    text_right_color: "#000000"
                    text: "Домой"
                    #on_press: app.root.manager.current = 'home'     Кнопка ,которая должна была работать, но не работает
                    

                DrawerClickableItem:
                    icon: "calendar-month"
                    text_right_color: "#000000"
                    text: "Календарь"
                    
                    
                DrawerClickableItem:
                    icon: "account-heart"
                    text: "Личный кабинет"
                    
                DrawerClickableItem:
                    icon: "medal"
                    text: "Достижения"

                MDNavigationDrawerDivider:

                MDNavigationDrawerLabel:
                    text: "Дополнительно"

                DrawerLabelItem:
                    icon: "anvil"
                    text: "Настройки"

                DrawerLabelItem:
                    icon: "arm-flex"
                    text: "Тех.поддержка"
'''

class HomeScreen(Screen):
    pass

class CalendarScreen(Screen):
    pass

class NavigationLayout(MDNavigationLayout):
    pass

class ContentNavigationDrawer(MDBoxLayout):
    pass

sm = ScreenManager()
sm.add_widget(HomeScreen(name='home'))
sm.add_widget(CalendarScreen(name='calendar'))

class SBSApp(MDApp):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(HomeScreen(name='home'))
        sm.add_widget(CalendarScreen(name='calendar'))
        self.theme_cls.theme_style = "Light"
        return Builder.load_string(MainPage)

if __name__ == '__main__':
    SBSApp().run()