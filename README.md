# blog_with_django

## Features

Let's determine some cases:

- it's a personal blog, so only admins can make posts;
- it could be posted just a post, poll or event;
- users can rate and comment posts.

## Posts

Let's determine that posts are html-like objects, that means admins can use all html5 features writing posts. This includes media files too

## Polls

Let's determine that the poll is something like a question with some answers. Question and answers are determined by publisher (admins). For each poll one user can choose at least one, but also more answers

## Event

It's pages in same styles with main cases: what event, where and when. Users can mark do they plan to attend the event
