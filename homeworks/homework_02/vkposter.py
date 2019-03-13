#!/usr/bin/env python
# coding: utf-8


from homeworks.homework_02.heap import MaxHeap
from homeworks.homework_02.fastmerger import FastSortedListMerger


class VKPoster:

    def __init__(self):
        self.post = {}
        self.userPost = {}
        self.subs = {}
        raise NotImplementedError

    def user_posted_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        выложил пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if user_id not in self.userPost.keys():
            self.userPost[user_id] = [post_id]
            # вводим в словарь юзера и пост по ключу и значению
        elif post_id not in self.userPost(user_id):
            self.userPost.get(user_id).append(post_id)
            # добавили новый пост к юзеру
        if post_id not in self.post.keys():
            self.post[post_id] = [user_id, []]

    def user_read_post(self, user_id: int, post_id: int):
        '''
        Метод который вызывается когда пользователь user_id
        прочитал пост post_id.
        :param user_id: id пользователя. Число.
        :param post_id: id поста. Число.
        :return: ничего
        '''
        if post_id not in self.post.keys():
            self.user_posted_post(-1, post_id)
        if user_id not in self.post.get(post_id)[1]:
            self.post.get(post_id)[1].append(user_id)

    def user_follow_for(self, follower_user_id: int, followee_user_id: int):
        '''
        Метод который вызывается когда пользователь follower_user_id
        подписался на пользователя followee_user_id.
        :param follower_user_id: id пользователя. Число.
        :param followee_user_id: id пользователя. Число.
        :return: ничего
        '''
        if follower_user_id not in self.sub.keys():
            self.sub[follower_user_id] = [followee_user_id]
            # add to sub
        else:
            self.sub[follower_user_id].append(follower_user_id)

    def get_recent_posts(self, user_id: int, k: int)-> list:
        '''
        Метод который вызывается когда пользователь user_id
        запрашивает k свежих постов людей на которых он подписан.
        :param user_id: id пользователя. Число.
        :param k: Сколько самых свежих постов необходимо вывести. Число.
        :return: Список из post_id размером К из свежих постов в
        ленте пользователя. list
        '''
        fast = [self.userPost.get(i) for subs in
                self.sub.get(user_id) if subs in
                self.userPost.keys()]
        return FastSortedListMerger.merge_first_k(fast, k)

        # not use FastSortedListMerger
        # post = list(self.post.keys())
        # post.sort(reverse=True)
        # recent_posts = [post_id for post_id in post
        #                if self.post.get(post_id)[0] in
        #                self.subs.get(user_id)]
        # return recent_posts[:k]

    def get_most_popular_posts(self, k: int) -> list:
        '''
        Метод который возвращает список k самых популярных постов за все время,
        остортированных по свежести.
        :param k: Сколько самых свежих популярных постов
        необходимо вывести. Число.
        :return: Список из post_id размером К из популярных постов. list
        '''
        # lets use MaxHeap
        h = MaxHeap([(len(self.post.get(i)[1]), i)
                     for i in list(self.post.keys())])
        return [h.extract_maximum()[1] for i in range(k)]
