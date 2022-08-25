from pytube import Channel, Playlist, YouTube

class Downloader:
    pass

# для скачивания видео
# video = YouTube('https://www.youtube.com/watch?v=gFRa6qVN980&list=PLDyJYA6aTY1lPWXBPk0gw6gR8fEtPDGKa&index=18')
# print(video.title)
# video.streams.filter(res="720p").first().download(output_path='E:\\Multimedia\\Cкачано с ютуба')
# print('Видео успешно скачано!)')

# для скачивания плейлиста
print('Введите URL плейлиста, который Вы хотите скачать')
while 'python':
    try:
        URL = input()
        play_list = Playlist(URL)

        print(f'Скачивается плейлист: {play_list.title}\n')
        result = 'all videos'
        not_downloaded_videos = []

        for video in play_list.videos:
            result = '100%'

            try:
                video.streams.filter(res="720p").first().download(output_path='E:\\Multimedia\\Cкачано с ютуба')
                print(f'{video.title} начинает скачиваться')
            except:
                result = 'not all videos'
                not_downloaded_videos.append(video.title)
                continue

        print()
        print('Весь плейлист успешно скачан!)' if result == 'all videos' else 'Не все видео скачаны')

        if len(not_downloaded_videos) > 0:
            for title in not_downloaded_videos:
                print(f'не скачано видео: {title}')

        print()
        break

    except KeyError:
        print('Вы не ввели URL. Попробуйте снова')

# print('Привет, Вы загрузили модуль способный скачать видео, плейлист или целый канал с You Tube!')
# print('Выберите, что именно Вы хотите скачать')
#
# print('Если Вы хотите скачать видео, то введите "видео"')
# print('Если Вы хотите скачать плейлист, то введите "плейлист"')
# print('Если Вы хотите скачать канал, то введите "канал"')
#
# while 'wrong answer':
#     try:
#         answer = input()
#     except:
#         print('Вы ввели неверные данные')
#
#
#     if answer.lower() == 'видео':
#         print('Подготавливаем видео к скачиванию')
#         break
#
#     elif answer.lower() == 'плейлист':
#         print('Подготавливаем плейлист к скачиванию')
#         break
#
#     elif answer.lower() == 'канал':
#         print('Подготавливаем канал к скачиванию')
#         break
#
#     else:
#         print('Вы выбрали неверную опцию')
#         print('Попробуйте снова')
