# This is a sample Python script.
from Model.Assets.Album.Album import Album
from Model.Assets.Artist.Artist import Artist
from Model.Assets.MusicApp.MusicApp import MusicApp
from Model.Assets.Song.Song import Song
from Model.Assets.Tag.Tag import Tag
from Model.Assets.User.User import User


# Press Mayús+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def set_app():
    app = MusicApp(r"C:\Users\Samuel\PycharmProjects\PROYECT_Storify\Model\Assets\MusicApp\muse.ic")

    a1 = Artist("001", "Kali", "USA", False)
    al1 = Album("Weather", "2017")
    a1.add_album(al1)
    app.add_artist(a1)
    s1 = Song("Hazel", "sh7agA", al1, a1, al1.year, 115, "pop", "https://www.youtube.com/watch?v=lp7SDPPbx-s")
    app.add_song(s1)

    a2 = Artist("002", "Mirella", "COL", False)
    al2 = Album("Lucero", "2018")
    a2.add_album(al2)
    app.add_artist(a2)
    s2 = Song("CruzDeSol", "a8a9HA", al2, a2, al2.year, 101, "lo-fi", "https://www.youtube.com/watch?v=lp7SDPPbx-s")
    app.add_song(s2)

    a3 = Artist("003", "Aztecombo", "MX", True)
    al3 = Album("SandiaWine", "2015")
    a3.add_album(al3)
    app.add_artist(a3)
    s3 = Song("Ganzua", "0A89lg", al3, a3, al3.year, 110, "rock", "https://www.youtube.com/watch?v=vKgqf1Bo_UI")
    app.add_song(s3)

    a4 = Artist("004", "Angy-G", "MX", False)
    al4 = Album("Alors", "2013")
    a4.add_album(al4)
    app.add_artist(a4)
    s4 = Song("Voux", "H97gAa", al4, a4, al4.year, 50, "pop", "https://www.youtube.com/watch?v=PrURjtcpBgU")
    app.add_song(s4)

    a5 = Artist("005", "Howler", "CDA", False)
    al5 = Album("Luxury", "2021")
    a5.add_album(al5)
    app.add_artist(a5)

    s5 = Song("Beach", "1la0AG", al5, a5, al5.year, 49, "pop", "https://www.youtube.com/watch?v=WSukD4Y_QY0")
    s5.add_tag(Tag("Trending"))
    s5.add_tag(Tag("Alelux"))
    s5.add_tag(Tag("Partrend"))
    s5.add_tag(Tag("Atrendding"))
    app.add_song(s5)

    print(str(s5.contains_true_tag(Tag("ding"))) + "\n")
    print(str(s5.contains_partial_tag(Tag("ding"))) + "\n")

    for song in app.get_songs():
        for tag in song.get_all_tags():
            print(song.get_name()+";"+tag.get_attribute()+" == Trend -> "+str(tag.get_compatibility(Tag("Trend"))))
    print("\n")

    for song in app.get_songs():
        for tag in song.get_all_tags():
            print(song.get_name()+";"+tag.get_attribute()+" == a -> "+str(tag.get_compatibility(Tag("a"))))
    print("\n")

    for song in app.get_songs():
        for tag in song.get_filtered_tags(Tag("a")):
            print(song.get_name()+";"+tag.get_attribute())
    print("\n")

    for song in app.get_songs():
        artist = song.get_artist()
        print(song.get_name()+";"+song.get_id()+";"+artist.get_name()+";"+song.get_url())
    print("\n")

    u1 = User("Carla", "torta2", "carton@gmail.com")
    app.add_user(u1)
    app.add_user_song(u1, s2)
    app.add_user_song(u1, s5)
    app.add_user_song(u1, s1)

    for song in u1.get_song_list():
        artist = song.get_artist()
        print(song.get_name() + ";" + song.get_id() + ";" + artist.get_name() + ";" + song.get_url())
    print("\n")

    u1.delete_song(s5)

    for song in u1.get_song_list():
        artist = song.get_artist()
        print(song.get_name() + ";" + song.get_id() + ";" + artist.get_name() + ";" + song.get_url())
    print("\n")

    u2 = User("Tomas", "torta2", "lordsith@gmail.com")
    u3 = User("Cecilia", "torta2", "clia@gmail.com")
    u4 = User("Diego", "torta2", "diegotelon@gmail.com")



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    set_app()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
