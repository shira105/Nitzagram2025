import pygame

from constants import *
from helpers import screen


class Post:
    """
    A class used to represent post on Nitzagram
    """
    def __init__(self,username,location,description):
        self.username=username
        self.location=location
        self.description=description
        self.counter_likes=0
        self.comments=[]
        #TODO: write me!
        pass

    def username(self):
        font = pygame.font.SysFont('chalkduster.ttf',UI_FONT_SIZE)
        text = font.render("CharliDamelio",True,BLACK)
        screen.blit(text,[USER_NAME_X_POS,USER_NAME_Y_POS])

    def add_likes(self):
        self.counter_likes+=1


    def likes(self):
        txt = "This post liked by",self.counter_likes, "people"
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        text = font.render(txt, True, BLACK)
        screen.blit(text, [DESCRIPTION_TEXT_X_POS,DESCRIPTION_TEXT_Y_POS])

    def Place(self):
        font = pygame.font.SysFont('chalkduster.ttf', UI_FONT_SIZE)
        text = font.render("Israel", True, BLACK)
        screen.blit(text, [DESCRIPTION_TEXT_X_POS,DESCRIPTION_TEXT_Y_POS])


    def display(self):
        """
        Display the Post image/Text, description, location, likes and comments
        on screen

        :return: None
        """
        pass

    def add_comment(self,comment):
        self.comments.append(comment)

    def post_content(self):
        pass

    def display_comments(self):

        """
        Display comments on post. In case there are more than 4
        comments, show only 4 comments chosen by reset_comments_display_index

        :return: None
        """
        position_index = self.comments_display_index
        # If there are more than 4 comments, print "view more comments"
        if len(self.comments) > NUM_OF_COMMENTS_TO_DISPLAY:
            comment_font = pygame.font.SysFont('chalkduster.ttf',
                                               COMMENT_TEXT_SIZE)
            view_more_comments_button = comment_font.render("view more comments",
                                                            True, LIGHT_GRAY)
            screen.blit(view_more_comments_button, (VIEW_MORE_COMMENTS_X_POS,
                                                    VIEW_MORE_COMMENTS_Y_POS))

        # Display 4 comments starting from comments_display_index
        for i in range(0, len(self.comments)):
            if position_index >= len(self.comments):
                position_index = 0
            self.comments[position_index].display(i)
            position_index += 1
            if i >= NUM_OF_COMMENTS_TO_DISPLAY - 1:
                break



