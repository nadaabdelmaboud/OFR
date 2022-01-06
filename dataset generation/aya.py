arr = [
    'وَالْحَيَاةَ لِيَبْلُوَكُمْ أَيُّكُمْ' ,
    'تَبَارَكَ الَّذِي بِيَدِهِ',
    'الْمُلْكُ وَهُوَ عَلَى',
    'الْكِتَابِ وَالجِنَّةِ',
    'الْمَلَائِكَةِ ',
    'الَّذِي خَلَقَ الْمَوْتَ',
    ' أَحْسَنُ عَمَلا ',
    'وَهُوَ الْعَزِيزُ الْغَفُورُ',
    'الَّذِي خَلَقَ سَبْعَ',
    'سَمَاوَاتٍ طِبَاقًا ',
    'مَّا تَرَى فِي خَلْقِ',
    'الرَّحْمَنِ مِن تَفَاوُتٍ',
    'الَّذِي خَلَقَ الْأَزْوَاجَ',
    'وَالثَّمَرَاتِ وَالْخَرَافَةِ',
    ' أَلَا يَعْلَمُ مَنْ خَلَقَ ',
    ' وَهُوَ اللَّطِيفُ الْخَبِيرُ ',
    ' وَهُوَ الْغَفُورُ الرَّحِيمُ',
    ' أَمْ أَمِنْتُمْ مَنْ',
    ' العلم خليل المؤمنين',
    'سبق السيف العذل',
    'رجع بخفي حنين',
    'أخذ بخفي حنين',
    'لسانك حصانك',
    'إنما نعطي',
    ' به نحو النجاح',
    'قطرة المطر',
    'تحفر في الصخر',
    ' ليس بالعنف',
    'لكن بالتكرار',
    'المرأة الفاضلة',
    'لكي تحافظ ',
    'ولا تحافظ على الأشخاص',
    'لا تحزن على طيبتك ',
    'قال أحد الحكماء ',
    'أنا أحب الأشخاص',
    'ليس من الذكاء',
    'ليس من الحكماء',
    ' أن تنتصر في الجدال',
    ' ألا تدخل في',
    'الامثال تشبه',
    'الي حد كبير الحكم',
    'والعبر والمواعظ ',
    'هي عبارة عن عبارة',
    'موجزة تقوم',
    'علي تشبيه حال',
    'او حادث محدد بهدف',
    'التعبير عن معني',
    'محدد وعادة ما',
    'إِنَّكَ لَمِنَ الْمُرْسَلِينَ',
    'لَقَدْ حَقَّ الْقَوْلُ',
    'إِنَّا جَعَلْنَا فِي',
    'إِنَّا نَحْنُ نُحْيِي',
    'وَجَاءَ مِنْ أَقْصَى ',
    'وَلَوْ نَشَاء',
    'أَفَلا يَشْكُرُونَ',
    'وَضَرَبَ لَنَا مَثَلا',
    'إِنَّمَا أَمْرُهُ',
    'إِنَّهُ عَلَى كُلِّ شَيْءٍ',
    'فَسُبْحَانَ الَّذِي',
    'أَنْزَلَ الْكِتَابُ',
    'الَّذِي بِيَدِهِ مَلَكُوتُ',
    'كُلِّ شَيْءٍ',
    'إِنَّ الْمُحْصِينَ',
    'فِي غَيْرِ الْحَقِّ',
    'ساعد اكتشاف',
    ' في القرن التاسع عشر',
    'واكتشاف عالم الآثار',
    ' أقدم من المصادر الأدبية',
    'على سبيل المثال',
    'يسبق ظهور أول تمثيل',
    ' الأدب ظهورها في',
    'الأدب الأصلي',
    'الإغريق مع تقدم الحضارة ',
    'شعب زراعي',
    'حيث بنوا خطاً ',
    'تفسير خلق العالم في',
    'عندما احتل كرونوس',
    'أَوَلَمْ يَرَوْا أَنَّا',
    'خَلَقْنَا لَهُمْ مِمَّا',
    'عَمِلَتْ أَيْدِينَا ',
    ' أَنْعَامًا فَهُمْ لَهَا',
    'وَذَلَّلْنَاهَا لَهُمْ فَمِنْهَا',
    'رَكُوبُهُمْ وَمِنْهَا يَأْكُلُونَ',
    'وَلَهُمْ فِيهَا',
    'مَنَافِعُ وَمَشَارِبُ أَفَلا',
    'وَاتَّخَذُوا مِن دُونِ',
    'لا يَسْتَطِيعُونَ نَصْرَهُمْ ',
    'فَلا يَحْزُنكَ قَوْلُهُمْ',
    'إِنَّا نَعْلَمُ مَا يُسِرُّونَ',
    'أَوَلَمْ يَرَ الإِنسَانُ',
    'وَضَرَبَ لَنَا مَثَلا',
    'وَنَسِيَ خَلْقَهُ قَالَ',
    'مَنْ يُحْيِي الْعِظَامَ',
    'قُلْ يُحْيِيهَا الَّذِي',
    ' أَنشَأَهَا أَوَّلَ مَرَّةٍ',
    'وَهُوَ الْخَلاَّقُ الْعَلِيمُ ',
    'قُتل رحمه الله',
    'عصفور في اليد',
    'خير من عشرة على',
    'عبارات و كلام عن اللغة',
    'لعربية من اقتباسات',
    ' و كلمات المشاهير ',
    'و الحكماء قمنا بجمعها',
    'الحسود لا يسود',
    ' جارك القريب',
    ' ولا أخوك البعيد',
    'ليس كل ما يلمع ذهبا',
    'إلي العربية الفصحي ',
    ' أساسياً لهذه ',
    'بمركزها العالمي ',
    'اجمل الحكم العربية',
    'من عفا ساد ',
    'ومن حلم عظم',
    'اعقل الناس',
    ' اعذرهم للناس',
    'احلم تسد',
    'هي من أبرز اللغات',
    ' لغة القرآن الكريم',
    'اللغة العربية هي ',
    'الآيات البينات لتكون',
    'واضحة العرب',
    'وبها معجزات لغوية',
    'وأقوال قليل الرزق',
    'مع سلامة النفس أمتع',
    ' من كثيره مع الأوجاع',
    'من يستعجل قطف ',
    ' العنب قبل نضوجه',
    'يأكله حامضاً',
    ' ليس الغريب غريب',
    'الشام واليمن',
    'من أكثر الأشياء الذي ',
    ' تجري الرياح',
    'بما لا تشتهي',
    'السفن حنانيك بعض',
    'أسطورة أفروديت ',
    'أسطورة زيوس',
    'أسطورة نرسيسوس',
    'أسطورة هرقل',
    ' يونانية مرعبة عن',
    'والشرقية له جسم أسد',
    'ورأس وأجنحة النسر',
    'وأحياناً رأس أفعى',
    'تكشف آية عبدالحافظ',
    'القديمة والتى كانت',
    ' تعد حضارة قوة',
    ' فى زمن ما',
    'كانت البناء الذى',
    'هذه القصص تتعلق ',
    ' أصل و طبيعة العالم',
    'نبات المرميدون',
    ' الناس الذين أتوا من النمل'
    ]