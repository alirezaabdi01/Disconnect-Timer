# Disconnect-Timer
A program to set timer for enabling or disabling a certain network adapter and more!

Adapter-Timer: Turning off or on a certain network adapter in a certain time

Click-Timer: Click on a certain place in a certain time

* Adapter-timer program needs administrative privilegess to run and will show an error if you didn't give it
* Add programs to your antivirus exceptions if your antivirus didn't allow the programs to run
* to see your list of adapters search 'Ncpa.cpl' in Run
* You can test that if you chose the correct adapter by disabling the adapter with the program
* Also do this for your mobile tethered to your pc for less disconnectivies: go to device manager and in the buttom find and select Universal Serial Bus controllers and select each one below it and if that device have power managment, turn off 'allow the computer to turn off this device to save power' https://youtu.be/mdWx4Ak8ca8?t=82
* \[For Android\] Also Turn on your phone developer mode and connect your phone to your pc and go to developer options in your phone settings and find and select 'Default USB Configuration' and select 'USB tethering'.


# Disconnect-Timer
پروژه ای حاوی برنامه های مخصوص دانلود کردن شبانه

Adapter-Timer : خاموش یا روشن کردن آداپتور اینترنت انتخاب شده در زمان مشخص

Click-Timer : کلیک کردن در مکان مشخص در زمان مشخص

این پروژه به شما کمک می کنه که بتونید سر ساعت شروع نت شبانه خود اینترت شبانه تون رو فعال کنید و موقع اتمام زمان نت شبانه اینترنت خودتون خاموش کنید. متاسفانه همچین قابلیتی برای گوشی ها که بشه از طریق گوشی اینترنت رو در یک زمان مشخص با یک برنامه خاموش کرد وجود نداره

مثال: شما اینترنت شبانه همراه اول خریدید. کاری که می تونید انجام بدید اینه که شما به طور مثال قبل از اینکه بخوابید که میشه قبل از ساعت 2 دانلود تون رو بزارید روی نت خونه تون و نت گوشی تون رو وصل کنید و آداپتور اش رو خاموش کنید. بعد 4 تا برنامه از Adapter-Timer رو باز می کنید یکی برای خاموش کردن آداپتور نت خونه ساعت 1:02 یکی روشن کردن آداپتور نت گوشی ساعت 1:02 یکی روشن کردن آداپتور نت خونه ساعت 10:58 دقیقه یکی خاموش کردن نت گوشی ساعت 10:58 (اگر که می خواستید دانلودتون متوقف نشه ولی اگه نخواستید می تونید آداپتور نت خونه رو روشن نکنید)

نکات برنامه ها:

* برای دیدن لیست آداپتور های سیستمتون Run رو باز کیند و Ncpa.cpl رو وارد کنید
* دو تا فایل رو داخل یک پوشه بریزید و اون پوشه رو به استثناهای آنتی ویروس تون اضافه کنید.
* برنامه Adapter-Timer نیاز به run as administator داره.
* قبل از زمان دادن به برنامه Adapter-Timer ، اول آداپتوری که انتخاب کردید رو خاموش و روشن کنید تا مطمئن بشید درست انتخاب کردید.
* مانیتورتون به صورت سخت افزاری خاموش نکنید و موس خود را از pc تون بیرون نکشید تا در روند برنامه click-timer مشکلی پیش نیاد.

چند نکته برای جلوگیری از اختلال در دانلود کردن با نت شبانه:

1- در سرچ ویندوز power and sleep رو سرچ کنید و گزینه اول رو انتخاب کنید و screen and sleep رو انتخاب کنید و دو گزینه sleep و turn off screen رو روی never بگذارید. می تونید turn off screen داشته باشید ولی برنامه click timer باید run as administator ران بشه تا موقعی که screen خاموشه کار بکنه.

2- وارد device manager بشید و Universal Serial Bus controllers رو پیدا کنید و روش کلیک کنید. هر کدوم از گزینه های پایینش رو کلیک کنید و اگر تب power managment داشت وارد اون بشید و تیک اولش رو بردارید ('allow the computer to turn off this device to save power'). بعضی اوقات سیستم خودش اتصالات usb رو ممکنه قطع کنه یا قطع و وصل کنه که با اینکار دیگه اتفاق نمی افته.

3- در گوشی خود developer mode رو روشن کنید (اسم شرکت گوشی تون رو سرچ کنید که چجوری میشه developer mode اش رو روشن کرد) بعد گوشی تون رو به سیستمی که می خواهید با اون دانلود کنید وصل کنید و وارد developers option تنظیمات گوشی تون بشید و گزینه Default USB Configuration رو پیدا کنید و واردش بشید بعد گزینه USB tethering رو انتخاب کنید. اینکار باعث میشه اگر هم سیم قطع و وصل شد، اینترنتش اتوماتیک وصل بشه.


اگر سوالی داشتید حتما در Issues بپرسید
