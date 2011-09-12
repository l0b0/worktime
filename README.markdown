worktime - Generate daily log web page
======================================

[Example file](https://github.com/l0b0/worktime/wiki/2010-12.xhtml)

Installation
------------

`sudo easy_install worktime`

Upgrade
-------

`sudo easy_install -U worktime`

Usage
-----
See `worktime --help`.

Examples
--------

Today's calendar: `worktime > today.xhtml`
The rest of the work week: `worktime -w --end $(date --date "Friday" +%Y-%m-%d) > week.xhtml`
December 31, 2011: `worktime --start 2011-12-31 --end 2011-12-31 > holiday.xhtml`
Weekdays of December 2011: `worktime --weekdays --start 2011-12 --end 2011 > Dec.xhtml`
Next weekend: `worktime --weekends --end $(date --date "Monday" +%Y-%m-%d) > weekend.xhtml`
