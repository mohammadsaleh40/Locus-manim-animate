from manim import *
import os
import warnings
PI_CREATURE_SCALE_FACTOR = 0.5

BODY_INDEX = 0
RIGHT_EYE_INDEX = 1+ 5
LEFT_EYE_INDEX = 2 + 5
LEFT_PUPIL_INDEX = 4+ 5
RIGHT_PUPIL_INDEX = 6+ 5
MOUTH_INDEX = 3+ 5

PI_CREATURE_DIR = "mydrawings/"


def get_norm(vec):
    return np.linalg.norm(vec)


class chaghCreature(SVGMobject):
    

    def __init__(self, mode="plain", **kwargs):
        
        self.color = RED
        self.file_name_prefix = "chagh2Creature"
        self.stroke_width = 0
        self.stroke_color = BLACK
        self.fill_opacity = 1.0
        #self.height = 3
        self.corner_scale_factor = 0.75
        self.flip_at_start = False
        self.is_looking_direction_purposeful = False
        self.start_corner = None
        # Range of proportions along body where arms are
        self.right_arm_range = [0.55, 0.7]
        self.left_arm_range = [.34, .462]
        self.pupil_to_eye_width_ratio = 0.4
        self.pupil_dot_to_pupil_width_ratio = 0.3
        #digest_config(self, kwargs)
        self.mode = mode
        self.parts_named = False
        
        svg_file = os.path.join(
            PI_CREATURE_DIR,
            "%s_%s.svg" % (self.file_name_prefix,mode)
        )
        print(svg_file)
        SVGMobject.__init__(self, file_name=svg_file, **kwargs)
        

        if self.flip_at_start:
            self.flip()
        print(self.start_corner)
        print(type(self.file_name_prefix))
        if self.start_corner is not None:
            self.to_corner(self.start_corner)

    def align_data(self, mobject):
        # This ensures that after a transform into a different mode,
        # the pi creatures mode will be updated appropriately
        SVGMobject.align_data(self, mobject)
        if isinstance(mobject, chaghCreature):
            self.mode = mobject.get_mode()
        
            
    def name_parts(self):
        self.mouth = self.submobjects[MOUTH_INDEX]
        self.body = self.submobjects[BODY_INDEX]
        left_pupil = VGroup(*[self.submobjects[LEFT_PUPIL_INDEX],
            self.submobjects[LEFT_PUPIL_INDEX+1],])
        print(self.submobjects)
        right_pupil = VGroup(*[self.submobjects[RIGHT_PUPIL_INDEX],
            self.submobjects[RIGHT_PUPIL_INDEX+1],])
        self.pupils = VGroup(*[left_pupil, right_pupil
        ])
        self.eyes = VGroup(*[
            self.submobjects[LEFT_EYE_INDEX],
            self.submobjects[RIGHT_EYE_INDEX]
        ])
        self.neghah = self.eyes.get_center()
        self.eye_parts = VGroup(self.eyes, self.pupils)
        self.parts_named = True
        
        

    def init_colors(self):
        SVGMobject.init_colors(self)
        if not self.parts_named:
            self.name_parts()
        self.mouth.set_fill(opacity=0)
        self.body.set_fill(self.color, opacity=1)
        self.eyes.set_fill(WHITE, opacity=1)
        self.submobjects[LEFT_PUPIL_INDEX+1].set_fill(WHITE, opacity = 1)
        self.submobjects[LEFT_PUPIL_INDEX+1].set_stroke(opacity = 0)
        self.submobjects[LEFT_PUPIL_INDEX+1].set(height = 3)
        self.submobjects[RIGHT_PUPIL_INDEX+1].set_fill(WHITE, opacity = 1)
        self.submobjects[RIGHT_PUPIL_INDEX+1].set_stroke(opacity = 0)
        self.submobjects[RIGHT_PUPIL_INDEX+1].set(height = 3)
        self.init_pupils()
        return self

    def init_pupils(self):
        pass
    
    #think my pupils are fine
    """
    def init_pupils(self):
        # Instead of what is drawn, make new circles.
        # This is mostly because the paths associated
        # with the eyes in all the drawings got slightly
        # messed up.
        for eye, pupil in zip(self.eyes, self.pupils):
            pupil_r = eye.get_width() / 2
            pupil_r *= self.pupil_to_eye_width_ratio
            dot_r = pupil_r
            dot_r *= self.pupil_dot_to_pupil_width_ratio

            new_pupil = Circle(
                radius=pupil_r,
                color=BLACK,
                fill_opacity=1,
                stroke_width=0,
            )
            dot = Circle(
                radius=dot_r,
                color=WHITE,
                fill_opacity=1,
                stroke_width=0,
            )
            new_pupil.move_to(pupil)
            pupil.become(new_pupil)
            dot.shift(
                new_pupil.get_boundary_point(UL) -
                dot.get_boundary_point(UL)
            )
            pupil.add(dot)
    """
    def copy(self):
        copy_mobject = SVGMobject.copy(self)
        copy_mobject.name_parts()
        return copy_mobject

    def set_color(self, color):
        self.body.set_fill(color)
        self.color = color
        return self

    def change_mode(self, mode):
        new_self = self.__class__(
            mode=mode,
        )
        new_self.match_style(self)
        new_self.match_height(self)
        if self.is_flipped() != new_self.is_flipped():
            new_self.flip()
        
        new_self.shift(self.eyes.get_center() - new_self.eyes.get_center())
        """
        if hasattr(self, "purposeful_looking_direction"):
            new_self.look(self.purposeful_looking_direction)
        """
        self.become(new_self)
        self.mode = mode
        return self

    def get_mode(self):
        return self.mode

    def look(self, direction):
        norm = get_norm(direction)
        if norm == 0:
            return
        direction /= norm
        self.purposeful_looking_direction = direction
        #change this to deal with the pupil having a white dot
        for pupil, eye in zip(self.pupils.split(), self.eyes.split()):
            c = eye.get_center()
            right = eye.get_right() - c
            up = eye.get_top() - c
            vect = direction[0] * right + direction[1] * up
            v_norm = get_norm(vect)
            p_radius = 0.5 * pupil.get_width()
            vect *= (v_norm - 0.75 * p_radius) / v_norm
            pupil.move_to(c + vect)
        self.pupils[1].align_to(self.pupils[0], DOWN)
        return self

    def look_at(self, point_or_mobject):
        self.neghah= point_or_mobject
        if isinstance(point_or_mobject, Mobject):
            point = point_or_mobject.get_center()
        else:
            point = point_or_mobject
        
        self.look(point - self.eyes.get_center())
        return self

    def change(self, new_mode, look_at_arg=None):
        self.change_mode(new_mode)
        if look_at_arg is not None:
            self.look_at(look_at_arg)
        return self

    def get_looking_direction(self):
        vect = self.pupils.get_center() - self.eyes.get_center()
        return normalize(vect)

    def get_look_at_spot(self):
        return self.eyes.get_center() + self.get_looking_direction()

    def is_flipped(self):
        return self.eyes.submobjects[0].get_center()[0] > \
            self.eyes.submobjects[1].get_center()[0]

    def blink(self):
        eye_parts = self.eye_parts
        eye_bottom_y = eye_parts.get_bottom()[1]
        middle_y = self.get_center()[1]
        eye_parts.apply_function(
            lambda p: [p[0], eye_bottom_y, p[2]]
        )
        return self

    def to_corner(self, vect=None, **kwargs):
        if vect is not None:
            SVGMobject.to_corner(self, vect, **kwargs)
        else:
            self.scale(self.corner_scale_factor)
            self.to_corner(DOWN + LEFT, **kwargs)
        return self

    def get_bubble(self, *content, **kwargs):
        bubble_class = kwargs.get("bubble_class", ThoughtBubble)
        bubble = bubble_class(**kwargs)
        if len(content) > 0:
            if isinstance(content[0], str):
                content_mob = TextMobject(*content)
            else:
                content_mob = content[0]
            bubble.add_content(content_mob)
            if "height" not in kwargs and "width" not in kwargs:
                bubble.resize_to_content()
        bubble.pin_to(self)
        self.bubble = bubble
        return bubble

    def make_eye_contact(self, pi_creature):
        self.look_at(pi_creature.eyes)
        pi_creature.look_at(self.eyes)
        return self

    def shrug(self):
        self.change_mode("shruggie")
        top_mouth_point, bottom_mouth_point = [
            self.mouth.points[np.argmax(self.mouth.points[:, 1])],
            self.mouth.points[np.argmin(self.mouth.points[:, 1])]
        ]
        self.look(top_mouth_point - bottom_mouth_point)
        return self

    def get_arm_copies(self):
        body = self.body
        return VGroup(*[
            body.copy().pointwise_become_partial(body, *alpha_range)
            for alpha_range in (self.right_arm_range, self.left_arm_range)
        ])


class Blink(ApplyMethod):

    def __init__(self, pi_creature, **kwargs):
        ApplyMethod.__init__(self, pi_creature.blink, **kwargs)

#set background color WHITE


