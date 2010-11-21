#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
NAME
       worktime - Generate daily log web pages

SYNOPSIS
       worktime [OPTION]... DIRECTORY

DESCRIPTION
       Creates a web page with a table on the left side showing the hours of
       the day, a table on the right showing the tasks of the day, and a space
       in the bottom right for notes.

       By default only today's log is created.

       Logs are created in DIRECTORY.

       Web site: <http://github.com/l0b0/worktime>

       -s, --start=DATE
             First date to print. Default today.

       -e, --end=DATE
             Last date to print. Default today.

       -d, --days=NAME...
             Create log files for only the given weekdays.

       -w, --weekdays
             Equivalent to "--days=Monday,Tuesday,Wednesday,Thursday,Friday".

       -W, --weekends
             Equivalent to "--days=Saturday,Sunday".

       -h, --help
             Print this documentation and exit.

EXAMPLES
       worktime --end=2011-12-31 ~/work
             Create a log file in ~/work for each day from today until
             2011-12-31.

       worktime --start=2010-12 --end=2011-02 --weekends ~/work
             Create a log file in ~/work for each Saturday and Sunday from
             2010-12-01 through 2011-02-28.

       worktime --weekdays --start=2012 --end=2012 ~/project-X
             Create a log file in ~/project-X for each week day of 2012.
"""

__author__ = 'Victor Engmark'
__copyright__ = 'Copyright (C) 2010 Victor Engmark'
__credits__ = ['Victor Engmark']
__maintainer__ = 'Victor Engmark'
__email__ = 'victor.engmark@gmail.com'
__license__ = 'GPL v3 or newer'

from calendar import monthrange
from datetime import date, timedelta
from getopt import getopt, GetoptError
from os.path import dirname, exists, join
from signal import signal, SIGPIPE, SIG_DFL
import sys

signal(SIGPIPE, SIG_DFL)
"""Avoid 'Broken pipe' message when canceling piped command."""

WEEKDAYS = [
    'Monday',
    'Tuesday',
    'Wednesday',
    'Thursday',
    'Friday',
    'Saturday',
    'Sunday']

HELP = 'See --help for more information.'

DATE_FORMAT = '%Y-%m-%d'


def worktime(start, end, days, directory):
    """
    Create worktime log files.

    @param start: Start date
    @param end: End date (exclusive)
    @param days: Iterable of weekdays to output
    @param directory: Where to put the log files
    """
    template_file = open(join(dirname(__file__), 'template.xhtml'))
    template = template_file.read()

    day_diff = end - start
    for index in range(day_diff.days):
        current = start + timedelta(days = index)
        if current.weekday() not in days:
            print 'Skipping %s' % WEEKDAYS[current.weekday()]
            continue

        # Establish output file
        output_path = join(directory, current.strftime(DATE_FORMAT) + '.xhtml')
        if exists(output_path):
            print 'Skipping existing worktime file %s' % output_path
            continue

        output_file = open(output_path, 'w')

        # Get template data
        current_printable = current.strftime('%A ' + DATE_FORMAT)

        # Write to template
        output_file.write(
            template % {
                'date': current_printable})


def usage():
    """Display documentation and exit."""
    print __doc__


def main(argv=None):
    """Argument handling."""

    if argv is None:
        argv = sys.argv

    start = date.today()
    end = start + timedelta(days = 1)
    days = range(7)

    try:
        opts, args = getopt(
            argv[1:],
            'sedwWhv',
            [
                'start=',
                'end=',
                'days=',
                'weekdays',
                'weekends',
                'help'])
    except GetoptError, err:
        sys.stderr.write(str(err) + '\n')
        return 2

    for option, value in opts:
        if option in ('-s', '--start'):
            values = [int(val) for val in value.split('-')]
            values.extend([1, 1][0:3-len(values)]) # Missing month and/or day

            start = date(values[0], values[1], values[2])
        elif option in ('-e', '--end'):
            values = value.split('-')
            if len(values) == 1:
                # Missing month and day
                values.extend([12, 31])
            elif len(values) == 2:
                # Missing day
                values.append(monthrange(values[0], values[1])[1])

            # Go to start of next day
            end = date(values[0], values[1], values[2]) + timedelta(days = 1)
        elif option in ('-d', '--days'):
            values = value.split(', ')

            # Get day numbers
            days = []
            for index in range(len(values)):
                try:
                    days[index] = WEEKDAYS.index(values[index])
                except ValueError, err:
                    print 'Unknown weekday %s. %s' % (values[index], HELP)
        elif option in ('-w', '--weekdays'):
            days = range(5)
        elif option in ('-W', '--weekends'):
            days = [5, 6]
        elif option in ('-h', '--help'):
            return usage()
        else:
            sys.stderr.write('Unhandled option %s\n' % option)
            return 2

    assert len(args) == 1, 'You have to specify a target directory. %s' % HELP
    directory = args[0]

    worktime(start, end, days, directory)


if __name__ == '__main__':
    sys.exit(main())
