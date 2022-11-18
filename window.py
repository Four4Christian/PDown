import PySimpleGUI as sg
import backend

sg.theme('DarkBlue2')

layout = [[sg.T('Insert video URL:'), sg.Input(size=(49,5),key='url')],
          [sg.T()],
          [sg.FolderBrowse('Download path'), sg.Input(size=(50,5), key='path')],
          [sg.T()],
          [sg.Button('DOWNLOAD')],
          [sg.T('v'), sg.T(f'{backend.v}'), sg.T(' '*68),sg.T('Made by: S4_Yuuki')]]

window = sg.Window('PDown', layout, size=(500,200),icon='pd.ico')

while True:
    event, values = window.read()

    if event == sg.WIN_CLOSED:
        break
    elif event == 'Hello World':
        print('Hello World')


    elif event == 'DOWNLOAD':
        #print(values['url'],values['path'])

        backend.url = values['url']
        backend.local = values['path']

        backend.download()

