# Challenge 1 - Subtask1:
## Dlaczego zdecydowałam się wziąć udział w wyzwaniu Dare IT?

Zdecydowałam się na udział w wyzwaniu, ponieważ mam podstawy testowania manualnego.
Chciałabym zobaczyć czym się to różni o testowania automatycznego.
W najbliższej przyszłości chciałabym się przebranżowić do IT.
Mam nadzieję, że **Dare IT Challenge** mi w tym pomoże.

*Monika*

![wynik_testu_purpurowego](https://github.com/moniakow/ChallengeOne/blob/main/image.png?raw=true)


# Challenge 2 - Subtask 2:
## Wypisz wszystkie elementy znajdujące się na stronie, a następnie, pod każdym elementem znalezionym na stronie, wymień 3 działające selektory.

*Sign in Button:*
* //*[text()="Sign in"]
* //*[@id="__next"]/form/div/div[2]/button/span[1]
* //*[contains(@class,"MuiTouchRipple")]
* //child::button/span[1]

*Select language*
* //*[text()="English"]
* //*[@id="__next"]/form/div/div[2]/div/div
* //parent::div/div

*Login input*
* //parent::div/div/div[1]/div
* //*[@id="__next"]/form/div/div[1]/div[1]/div
* //*[@class="MuiInputBase-root MuiInput-root MuiInput-underline MuiInputBase-formControl MuiInput-formControl"]
* //*[@id="login"]

*Password input*
* //parent::div/div/div[2]/div
* //*[@id="__next"]/form/div/div[1]/div[2]/div
* //*[@id="password"]

*Remind Password hyperlink*
* //*[@id="__next"]/form/div/div[1]/a
* //*[text()="Remind password"]
* //child::div/a