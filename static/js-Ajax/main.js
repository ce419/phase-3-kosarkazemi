var getPersianDateString = function (datetime) {
    var monthNames = ['Farvardin', 'Ordibehesht', 'Khordad', 'Tir', 'Mordad', 'Shahrivar',
        'Mehr', 'Aban', 'Azar', 'Dey', 'Bahman', 'Esfand'];
    var date = new Date(datetime);
    var sec = date.getSeconds();
    var min = (date.getMinutes() + 30) % 60;
    var hour = (date.getHours() + 4 + Math.floor((date.getMinutes() + 30) / 60)) % 24;
    var persian = persianDate(date);
    return monthNames[persian.pDate.month - 1] + ' ' + persian.pDate.monthDayNumber + ' ' + persian.pDate.year + ', ' + hour + ':' + min + ':' + sec;
};