"""Dataset sederhana: 30 deskripsi makanan/minuman dalam 3 kategori."""

documents = [
    # Makanan berat (10)
    {"text": "Nasi goreng adalah nasi yang ditumis bersama bumbu, telur, dan kecap hingga harum.", "category": "makanan_berat"},
    {"text": "Mie ayam merupakan mie dengan topping potongan ayam berbumbu dan sayuran.", "category": "makanan_berat"},
    {"text": "Bakso adalah bola daging yang disajikan dalam kuah hangat bersama mie atau bihun.", "category": "makanan_berat"},
    {"text": "Soto ayam adalah sup tradisional berisi ayam, kuah rempah, dan pelengkap seperti telur.", "category": "makanan_berat"},
    {"text": "Rendang dibuat dari daging sapi yang dimasak lama menggunakan santan dan rempah.", "category": "makanan_berat"},
    {"text": "Ayam geprek terdiri dari ayam goreng tepung yang ditumbuk bersama sambal pedas.", "category": "makanan_berat"},
    {"text": "Gado-gado merupakan sayuran rebus dengan tahu, telur, dan saus kacang.", "category": "makanan_berat"},
    {"text": "Nasi uduk adalah nasi gurih yang dimasak dengan santan dan disajikan bersama lauk.", "category": "makanan_berat"},
    {"text": "Sate ayam merupakan potongan daging ayam yang ditusuk lalu dibakar dan disajikan dengan bumbu kacang.", "category": "makanan_berat"},
    {"text": "Bubur ayam adalah bubur nasi lembut yang diberi suwiran ayam dan pelengkap gurih.", "category": "makanan_berat"},
    # Camilan (10)
    {"text": "Pisang goreng adalah irisan pisang yang dibalut adonan lalu digoreng hingga renyah.", "category": "camilan"},
    {"text": "Martabak manis adalah kue tebal dengan isian cokelat, keju, atau kacang.", "category": "camilan"},
    {"text": "Brownies merupakan kue cokelat dengan tekstur padat dan rasa manis.", "category": "camilan"},
    {"text": "Donat adalah roti goreng berbentuk cincin yang sering diberi gula atau topping.", "category": "camilan"},
    {"text": "Cireng terbuat dari tepung tapioka yang digoreng dan biasa dimakan bersama saus.", "category": "camilan"},
    {"text": "Roti bakar adalah roti yang dipanggang dengan isian selai, cokelat, atau keju.", "category": "camilan"},
    {"text": "Klepon adalah jajanan tradisional berbahan ketan berisi gula merah dan ditaburi kelapa.", "category": "camilan"},
    {"text": "Kentang goreng merupakan potongan kentang yang digoreng hingga garing dan diberi garam.", "category": "camilan"},
    {"text": "Pempek adalah olahan ikan dan tepung yang disantap dengan kuah cuko asam pedas.", "category": "camilan"},
    {"text": "Puding cokelat adalah makanan penutup dingin dengan tekstur lembut dan rasa cokelat.", "category": "camilan"},
    # Minuman (10)
    {"text": "Es teh manis adalah seduhan teh bercampur gula yang disajikan dengan es batu.", "category": "minuman"},
    {"text": "Kopi susu dibuat dari campuran kopi, susu, dan kadang gula aren.", "category": "minuman"},
    {"text": "Jus alpukat adalah minuman kental dari buah alpukat yang diblender bersama air atau susu.", "category": "minuman"},
    {"text": "Es jeruk dibuat dari perasan jeruk segar yang disajikan dingin.", "category": "minuman"},
    {"text": "Wedang jahe adalah minuman hangat berbahan jahe dan gula yang terasa pedas ringan.", "category": "minuman"},
    {"text": "Cokelat panas adalah minuman hangat dari bubuk cokelat dan susu.", "category": "minuman"},
    {"text": "Matcha latte merupakan campuran bubuk teh hijau dan susu yang dapat disajikan dingin atau hangat.", "category": "minuman"},
    {"text": "Es kelapa muda adalah minuman segar yang berisi air kelapa dan daging kelapa muda.", "category": "minuman"},
    {"text": "Smoothie stroberi dibuat dengan menghaluskan buah stroberi dan yoghurt atau susu.", "category": "minuman"},
    {"text": "Lemon tea adalah teh dengan rasa lemon yang biasa disajikan segar dan dingin.", "category": "minuman"},
]
