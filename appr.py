from flask import Flask, render_template

app = Flask(__name__)

restaurants = [
    {
        "id": 1,
        "location": "Girona, Spain",
        "restaurant_name": "El Celler de Can Roca",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/R.e55920d5b0d2477578e2af0e5791d3b4?rik=Rce2g3hh%2f9aaRg&riu=http%3a%2f%2f3.bp.blogspot.com%2f-9ORaKmKQ94A%2fUh0OK9vzPYI%2fAAAAAAAAZZE%2fcBAHEFL-kgI%2fs1600%2fEl-Celler-de-Can-Roca.jpg&ehk=Wh6G3OvqokVMFNhUWa59a31NhdEbQOCrD216CO0MJhM%3d&risl=&pid=ImgRaw&r=0"
    },
    {
        "id": 2,
        "location": "Modena, Italy",
        "restaurant_name": "Osteria Francescana",
        "status": "Open",
        "image_url": "https://robbreport.com.my/wp-content/uploads/2016/07/FEATOsteriaFrancescana_1.jpg"
    },{
        "id": 3,
        "location": "Hong Kong",
        "restaurant_name": "Bo Innovation",
        "status": "Open",
        "image_url": "https://secure.s.forbestravelguide.com/img/properties/Property-BoInnovation-Restaurant-1-Style-DiningRoom-CreditBoInnovation.jpg"
    },{
        "id": 4,
        "location": "Copenhagen, Denmark",
        "restaurant_name": "Noma",
        "status": "Closed",
        "image_url": "https://media.architecturaldigest.in/wp-content/uploads/2018/05/Noma2018_1422-866x487.jpg"
    },{
        "id": 5,
        "location": "London, UK",
        "restaurant_name": "Dishoom",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.CsVRCSQd3t84kd4Mx5sAhAHaFX?rs=1&pid=ImgDetMain"
    },{
        "id": 6,
        "location": "Maldives",
        "restaurant_name": "Ithaa Undersea Restaurant",
        "status": "Open",
        "image_url": "https://www.pandotrip.com/wp-content/uploads/2014/05/Ithaa-Restaurant4.jpg"
    },{
        "id": "7",
        "location": "Hong KOng",
        "restaurant_name": "Tim Wo Han",
        "status": "Closed",
        "image_url": "https://timhowan.jp/_img/location/03.jpg"
    },{
        "id": "8",
        "location": "Lima, Peru",
        "restaurant_name": "Maido",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/R.b0282f71efbcbf347688df76227d3ef8?rik=wWT6Zgcc%2bXpleA&riu=http%3a%2f%2fwww.cheryltiu.com%2fwp-content%2fuploads%2f2018%2f03%2fMitsuharu-Tsumuras-Aji-Restaurant-at-MGM-Cotai-Macau-China-Photo-by-Cheryl-Tiu-e1520443426705-1024x617.jpg&ehk=UfrflI4BBr%2fATEj97ZUDLDDDILOBrZhrmLvyUhqKnes%3d&risl=&pid=ImgRaw&r=0"
    },{
        "id": "9",
        "location": "Mexico City, Mexico",
        "restaurant_name": "Quintonil",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/24/7e/64/80/quintonil.jpg"
    },{
        "id": "10",
        "location": "Bangkok, Thailand",
        "restaurant_name": "Gaggan",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.iWuC6uowXEzG2NNJfBd51QHaEx?rs=1&pid=ImgDetMain"
    },{
        "id": "11",
        "location": "Paris, France",
        "restaurant_name": "Septime",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OLC.v5hRzSxDv05bJA480x360?&rs=1&pid=ImgDetMain"
    },{
        "id": "12",
        "location": "Bogota, Colombia",
        "restaurant_name": "El Chato",
        "status": "Open",
        "image_url": "https://www.theworlds50best.com/filestore/W50BR24/El%20Chato-exterior%20W50BR24%20profile.jpeg"
    },{
        "id": "13",
        "location": "Antwerp, Belgium",
        "restaurant_name": "The Jane",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.hnWJ8QFiNfWnSkDmGhULzAHaFn?rs=1&pid=ImgDetMain"
    },{
        "id": "14",
        "location": "Stockholm, Sweden",
        "restaurant_name": "Frantzen",
        "status": "Open",
        "image_url": "https://cdn.vox-cdn.com/thumbor/Y4SToYD1KxZWILPeSbkYymG56tk=/0x0:2000x1333/2120x1413/filters:focal(840x507:1160x827)/cdn.vox-cdn.com/uploads/chorus_image/image/56672181/_DS_5955.0.jpg"
    },{
        "id": "15",
        "location": "New York, USA",
        "restaurant_name": "Le Bernardin",
        "status": "Open",
        "image_url": "https://vrconcierge.com/wp-content/uploads/2021/03/le-bernardin-new-york-ny-exterior-1.jpg"
    },{
        "id": "16",
        "location": "Buenos Aires, Argentina",
        "restaurant_name": "Don Julio",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.QW_0VsA0Y2xjypqsFZ6EzgHaEK?rs=1&pid=ImgDetMain"
    },{
        "id": "17",
        "location": "Dubai, UAE",
        "restaurant_name": "Tresind Studio",
        "status": "Open",
        "image_url": "https://th.bing.com/th?id=OLC.JRbeE6+sEQYb2w480x360&rs=1&pid=ImgDetMain"
    },{
        "id": "18",
        "location": "London, England",
        "restaurant_name": "Kol",
        "status": "Open",
        "image_url": "https://img.cardapio.menu/storage/media/company_images/31395864/conversions/thumbnail.jpg"
    },{
        "id": "19",
        "location": "Tokyo, Japan",
        "restaurant_name": "Sezanne",
        "status": "Open",
        "image_url": "https://elitetraveler.com/wp-content/uploads/sites/8/2022/04/MAR_1198-1-min.jpg"
    },{
        "id": "20",
        "location": "Melbourne, Australia",
        "restaurant_name": "Attica",
        "status": "Closed",
        "image_url": "https://lh3.googleusercontent.com/places/ANJU3DtLFdpJY0bKcglcdQgzQqZuIsYlwwrXvv9-mnPtLlCYxJOa_hPqUmZ-n0-K7Ey3JNjCHLQlIe7QIweAv6hAMdZB5r_go9Gbyw=s1600-w480"
    },{
        "id": "21",
        "location": "Vienna, Austria",
        "restaurant_name": "Steirereck",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.-d-lWtfeI8hW2SKy401LDQHaFj?rs=1&pid=ImgDetMain"
    },{
        "id": "22",
        "location": "Sao Paulo, Brazil",
        "restaurant_name": "A Casa do Porco",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.z7NfJBvX5XgIK_AZ_6kqiAHaFj?rs=1&pid=ImgDetMain"
    },{
        "id": "23",
        "location": "Toronto, Canada",
        "restaurant_name": "Alo Restaurant",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.BFIl-0_z5pN8MoQX8Vc2kwHaE8?rs=1&pid=ImgDetMain"
    },{
        "id": "24",
        "location": "Santiago, Chile",
        "restaurant_name": "Borago",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.i438dQIsqwz5d_HkirmUHgHaFD?rs=1&pid=ImgDetMain"
    },{
        "id": "25",
        "location": "Hong Kong, China",
        "restaurant_name": "The Chairman",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.gUnRgjA5p1EaDW3DxnQNOQHaEx?rs=1&pid=ImgDetMain"
    },{
        "id": "26",
        "location": "Cairo, Egypt",
        "restaurant_name": "Abou El Sid",
        "status": "Open",
        "image_url": "https://cdn.tasteatlas.com/images/restaurants/44c105d8f6874a6290a61c53175970a3.jpg?mw=1300"
    },{
        "id": "27",
        "location": "Berlin, Germany",
        "restaurant_name": "Restaurant Tim Raue",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.Azo7zb0-85SwioWMNAIJEAHaEK?rs=1&pid=ImgDetMain"
    },{
        "id": "28",
        "location": "Athens, Greece",
        "restaurant_name": "Funky Gourmet",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.56AxhqhADdKee7CcxiEavAHaE8?rs=1&pid=ImgDetMain"
    },{
        "id": "29",
        "location": "Bali, Indonesia",
        "restaurant_name": "Nusa Gastronomy",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.I_OUtRror3GxfWqqV3JCcwAAAA?rs=1&pid=ImgDetMain"
    },{
        "id": "30",
        "location": "Dublin, Ireland",
        "restaurant_name": "Chapter One",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.zfY7F45doS3b7R-lCODEiwHaDP?rs=1&pid=ImgDetMain"
    },{
        "id": "31",
        "location": "Beirut, Lebanon",
        "restaurant_name": "Tawlet",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.jjLNktOEr0ADi3HDF1n2DwHaE1?rs=1&pid=ImgDetMain"
    },{
        "id": "32",
        "location": "Kuala Lumpur, Malaysia",
        "restaurant_name": "Dewakan",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.ho95mya7SDy4Bi63s5dr8QHaE7?rs=1&pid=ImgDetMain"
    },{
        "id": "33",
        "location": "Zwolle, Netherlands",
        "restaurant_name": "De Librijie",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.4E4beJdE4SWC1ADxyEmiVgHaE8?rs=1&pid=ImgDetMain"
    },{
        "id": "34",
        "location": "Oslo, Norway",
        "restaurant_name": "Maaemo",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.lzCed-7k4ri0nzY5KTPuMwHaE8?rs=1&pid=ImgDetMain"
    },{
        "id": "35",
        "location": "Quezon City, Philippines",
        "restaurant_name": "Pepeton's Grill & Catering",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.grnCzfwBqWNEqwlW9oTihwHaJ4?rs=1&pid=ImgDetMain"
    },{
        "id": "36",
        "location": "Lisbon, Portugal",
        "restaurant_name": "Belcanto",
        "status": "Closed",
        "image_url": "https://th.bing.com/th/id/OIP.9MogSOYsilcs3FeLbSmUsQHaE8?rs=1&pid=ImgDetMain"
    },{
        "id": "38",
        "location": "Singapore",
        "restaurant_name": "Odette",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.fsAbyEUl1CyflB4L63cSNQHaFR?rs=1&pid=ImgDetMain"
    },{
        "id": "39",
        "location": "Cape Town, South Africa",
        "restaurant_name": "La Colombe",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.wnPdKlRbmqm0p9taTQPINAHaE1?rs=1&pid=ImgDetMain"
    },{
        "id": "40",
        "location": "Seoul, South Korea",
        "restaurant_name": "Mingles",
        "status": "Open",
        "image_url": "https://www.theworlds50best.com/discovery/filestore/jpg/Mingles-Seoul-Korea-02.jpg"
    },{
        "id": "41",
        "location": "Furstenau, Switzerland",
        "restaurant_name": "Schloss Schauenstein",
        "status": "Open",
        "image_url": "https://axwwgrkdco.cloudimg.io/v7/__gmpics__/d3a11d13d0724361a33c62aae5ca2fc7"
    },{
        "id": "42",
        "location": "Taipei, Taiwan",
        "restaurant_name": "MUME",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.IDCrHO6wvjRg0tyfuacKSAHaFS?rs=1&pid=ImgDetMain"
    },{
        "id": "43",
        "location": "Istanbul, Turkey",
        "restaurant_name": "Mikla",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.yC2TXov0Nc9fhsPANggXvAHaE7?rs=1&pid=ImgDetMain"
    },{
        "id": "44",
        "location": "Ho Chi Minh City, Vietnam",
        "restaurant_name": "Anan Saigon",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.rn64pqIvQ6gu_BMCFKkolgHaE6?rs=1&pid=ImgDetMain"
    },{
        "id": "45",
        "location": "Paranaque, Philippines",
        "restaurant_name": "Gordon Ramsay Bar & Grill Ph",
        "status": "Open",
        "image_url": "https://dynamic-media-cdn.tripadvisor.com/media/photo-o/2d/5a/eb/4f/caption.jpg"
    },{
        "id": "46",
        "location": "Intramuros, Manila",
        "restaurant_name": "Illustrado Restaurant",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.kFixSB4-GJeMXFomOz2bkAHaE9?rs=1&pid=ImgDetMain"
    },{
        "id": "47",
        "location": "Taguig, Philippines",
        "restaurant_name": "Las Flores",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.ieMgK3hWGg14_Cw_jfouogHaE_?rs=1&pid=ImgDetMain"
    },{
        "id": "48",
        "location": "Tagaytay, Philippines",
        "restaurant_name": "Antonio's Restaurant",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.SVHyX5Zq5GKNj5zLxO-spwHaE6?rs=1&pid=ImgDetMain"
    },{
        "id": "49",
        "location": "Cebu City, Philippines",
        "restaurant_name": "Abaca Restaurant",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.D3h2-sQfZ6UYNGRbl5gyDwHaEK?rs=1&pid=ImgDetMain"
    },{
        "id": "50",
        "location": "Davao City, Philippines",
        "restaurant_name": "Bistro Selera",
        "status": "Open",
        "image_url": "https://th.bing.com/th/id/OIP.CHtXuld_5hZsVVaNbGk1RgHaE6?rs=1&pid=ImgDetMain"
    }
]

@app.route('/')
def hello_world():
    return render_template('index.html', title="Restaurants around the World", restaurants=restaurants)


if __name__ == '__main__':
    app.run(debug=True)