
function darkTheme(Theme, brightTheme, color){
    var main_section = document.getElementById('main-section');
    var darkmode = document.getElementById('darkmode');
    if (darkmode.style.color != 'black') {
        darkmode.style.color = 'black'
        darkmode.style.transform = 'translateX(1.3rem)'
        main_section.className=Theme
        
    } else {
        darkmode.style.color = color
        main_section.className= brightTheme
        darkmode.style.transform = 'translateX(-.6rem)'
    }
}


//Function for the dark mode
var dark = document.getElementById('dark');
dark.addEventListener('click', () => {
   darkTheme('darkTheme', 'brightTheme', 'white')
});

function themeChanger(Theme,color){
    var main_section = document.getElementById('main-section');
    var darkmode = document.getElementById('darkmode');
        darkmode.style.color = color
        main_section.className=Theme      
}


//customized send button
chat_icon5 = document.getElementById('chat-icon5')
chat_icon5.addEventListener('mousedown', () => {
    chat_icon5.style.transform = 'scale(.9)';
})
chat_icon5.addEventListener('mouseup', () => {
    chat_icon5.style.transform = 'scale(1)';
})