function int(a) {
  return Math.floor(a);
}
var Time = {
  MILLISECONDS: 1,
  SECONDS: 1e3,
  MINUTES: 6e4,
  HOURS: 36e5,
  DAYS: 864e5,
  daysInMonth: [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31],
  totalYears: 0,
  remainingYears: 0,
  totalMonths: 0,
  remainingMonths: 0,
  totalDays: 0,
  remainingDays: 0,
  totalHours: 0,
  remainingHours: 0,
  totalMinutes: 0,
  remainingMinutes: 0,
  totalSeconds: 0,
  remainingSeconds: 0,
  totalMilliseconds: 0,
  remainingMilliseconds: 0,
  calcTime: function(a, b) {
    startDate = new Date(a),
    endDate = new Date(b);
    
    var c = endDate.getTime() - startDate.getTime();
    
    Time.totalMilliseconds = c / Time.MILLISECONDS,
    Time.totalSeconds = c / Time.SECONDS,
    Time.totalMinutes = c / Time.MINUTES,
    Time.totalHours = c / Time.HOURS,
    Time.totalDays = c / Time.DAYS,
    Time.totalMonths = Time.calcTotalMonths(Time.totalDays, startDate),
    Time.totalYears = Time.totalMonths / 12,
    Time.remainingYears = int(Time.totalYears),
    Time.remainingMonths = int(Time.totalMonths - 12 * Time.remainingYears),
    Time.remainingDays = 
      int(Time.totalDays - Time.getDaysFromMonths(startDate, Time.totalMonths)),
    Time.remainingHours = int(Time.totalHours - 24 * int(Time.totalDays)),
    Time.remainingMinutes = int(Time.totalMinutes - 60 * int(Time.totalHours)),
    Time.remainingSeconds =
      int(Time.totalSeconds - 60 * int(Time.totalMinutes)),
    Time.remainingMilliseconds =
      int(Time.totalMilliseconds - 1e3 * int(Time.totalSeconds));
  },
  isLeapYear: function(a) {
    return a > 0 && !(a % 4) && (a % 100 || !(a % 400));
  },
  calcTotalMonths: function(a, b) {
    for (
      var c = b.getMonth(),
        d = b.getFullYear(),
        e = c,
        f = d,
        g = 0;
      a > Time.daysInMonth[e];
    ){
      a -= Time.daysInMonth[e],
      2 == e && Time.isLeapYear(f) && (a -= 1),
      e++,
      12 == e && (e = 0, f++),
      g++;
    }
    var h = a / Time.daysInMonth[e];
    return g + h;
  },
  getDaysFromMonths: function(a, b) {
    b = int(b);
    for (
      var c = a.getMonth(),
        d = a.getFullYear(),
        e = c,
        f = d,
        g = 0,
        h = 0;
      b > h;
      h++
    ){
      g += Time.daysInMonth[e],
        2 == e && Time.isLeapYear(f) && (g += 1),
        e++,
        12 == e && (e = 0, f++);
    }
    return g;
  }
};
