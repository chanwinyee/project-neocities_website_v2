Title: Building a Study Schedule
Date: 2023-08-11 17:00
Modified: 2023-08-12 16:45
Category: Journal
Tags: journal, how_to
Slug: building-study-schedule
Authors: chanwinyee
Summary: How to use the power of gSheet to make a semi-automated reading schedule.
Gallery: {photo}/j-20230811/

When working from books to learn something new, I know that the author has a learning plan set which is commonly found in the introduction or an "About this Book" section. The issue for self-guided learning is understanding how that book's structure fits into my current ability to read/concentrate on this topic week-on-week. 

**The goal of this article is to break down book-guided learning into consumable pieces using Google Sheets and a bit of automation.**

By breaking down books into pieces that both follow the author's intended learning structure and respect my personal constraints, I am set up for continuous forward motion on multiple pursuits. Sure, progress at times may feel slow, but forward motion is always a positive gain. 

Some of the constraints I deal with are - time, attention span, and fear of that "stuck" feeling where I am just not progressing on my project aspirations. (More constraints are best explained in my [Learn to Study Guide](https://docs.google.com/document/d/178_iYoByP8EPwmccpEoYohAQSfpDNdsAyH22KCCxYYg/edit?usp=sharing).)

To respect these constraints, I designed a reading schedule that:
- Sets weekly reading assignments (not monthly or daily)
- Alerts me when the study load is going beyond my upper bound or is highly optimistic during times of ... you know... life.

So, how can I make something that gives me this information? Google Sheets! 

When I first set up this spreadsheet (V1 and V2), it was painstakingly manual and, worse, it was inflexible. I had the most friction with:

- Getting week start dates (other than looking at a calendar)
- Manually entering start and finish reading position for each chapter (even with some clunky formulas)
- Re-working the entire manual process when I needed to make customizations
- New years, new books required a repeat of this slow-and-painful data entry process making me question my goals in life

After 2-3 years of tinkering, I landed on a data model-inspired ecosystem and used the power of sheet =QUERY() and data validation to semi-automate this process.

<img src="/images/inline/20230811-datamodel_reading_schedule.jpg">

Key features:

- Easily pick any book from desired interests with a one-time set up
- Drop down menus to assign chapters with automated population of chapter attributes (such as start, end pages)
- Drop down book selection
- Week of Year (WoY) implementation to simplify week-start date settings

At a high-level, set up for this type of study guide schedule is quite simple and does not require an advance degree in excel. 

Skills required:

- =CONCAT()
- =VLOOKUP()
- =QUERY()
- Data Entry and patience (but only one time per book!)

Steps:

1. Set up a dates sheet that has the columns: nixes, week of year, dates, day of week
2. Set up book details with columns: index, title, chapter, start, finish, total pages, ...
3. Use VLOOKUP to reference dates based on dates.index = CONCAT(week of year, date, day of week)
4. Set data validation (which automatically filters to distinct values in a column) for Book Title (row 1:1), Chapter, etc.
5. Use =QUERY() on schedule sheet some rows down to pull in the chapter and pages columns.
6. Set data validation on the schedule sheet for chapter names in the main schedule section.
7. Use VLOOKUP to reference book and chapter to get start-finish attributes.

If you are planning to make this schedule and have questions or want templates, DM me! I am more than happy to assist. :) Good luck!
