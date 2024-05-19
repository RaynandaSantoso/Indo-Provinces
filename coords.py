import turtle
import pandas as pd


# def get_mouse_click_coor(x, y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()


Provinces = {
    'Aceh': (-356.0, 89.0),
    'Sumatera Utara': (-318.0, 57.0),
    'Riau': (-271.0, 18.0),
    'Sumatera Barat': (-295.0, 2.0),
    'Jambi': (-253.0, -20.0),
    'Bengkulu': (-272.0, -45.0),
    'Lampung': (-208.0, -75.0),
    'Sumatera Selatan': (-231.0, -38.0),
    'Bangka Belitung': (-195.0, -24.0),
    'Banten': (-206.0, -103.0),
    'Dki Jakarta': (-186.0, -91.0),
    'Jawa Barat': (-175.0, -110.0),
    'Jawa Tengah': (-135.0, -114.0),
    'Yogyakarta': (-124.0, -130.0),
    'Jawa Timur': (-89.0, -120.0),
    'Bali': (-34.0, -137.0),
    'Nusa Tenggara Barat': (5.0, -138.0),
    'Nusa Tenggara Timur': (67.0, -140.0),
    'Papua Selatan': (361.0, -111.0),
    'Papua Pegunungan': (367.0, -76.0),
    'Papua Tengah': (311.0, -62.0),
    'Papua': (344.0, -34.0),
    'Papua Barat': (264.0, -21.0),
    'Maluku': (203.0, -46.0),
    'Maluku Utara': (174.0, 25.0),
    'Sulawesi Utara': (119.0, 31.0),
    'Gorontalo': (78.0, 23.0),
    'Sulawesi Tengah': (54.0, -11.0),
    'Sulawesi Barat': (21.0, -36.0),
    'Sulawesi Selatan': (42.0, -67.0),
    'Sulawesi Tenggara': (82.0, -64.0),
    'Kalimantan Selatan': (-31.0, -46.0),
    'Kalmantan Tengah': (-76.0, -24.0),
    'Kalimantan Barat': (-123.0, 16.0),
    'Kalimantan Timur': (-17.0, 20.0),
    'Kalimantan Utara': (-16.0, 74.0),
    'Kepulauan Riau': (-193.0, 72.0)
}

# df = pd.DataFrame.from_dict(Provinces, orient="index")
# df2 = df.rename(columns={'Unnamed: 0':'Provinsi'}, inplace=True )
# df2.to_csv("381_Province.csv")
