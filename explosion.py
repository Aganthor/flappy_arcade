import arcade


class PlaneExplosion(arcade.Sprite):
    def __init__(self):
        super().__init__()

        self.textures = [
            arcade.load_texture("assets/images/smokeparticles/PNG/Explosion/explosion00.png"),
            arcade.load_texture("assets/images/smokeparticles/PNG/Explosion/explosion01.png"),
            arcade.load_texture("assets/images/smokeparticles/PNG/Explosion/explosion02.png"),
            arcade.load_texture("assets/images/smokeparticles/PNG/Explosion/explosion03.png"),
            arcade.load_texture("assets/images/smokeparticles/PNG/Explosion/explosion04.png"),
            arcade.load_texture("assets/images/smokeparticles/PNG/Explosion/explosion05.png"),
            arcade.load_texture("assets/images/smokeparticles/PNG/Explosion/explosion06.png"),
            arcade.load_texture("assets/images/smokeparticles/PNG/Explosion/explosion07.png"),
            arcade.load_texture("assets/images/smokeparticles/PNG/Explosion/explosion08.png"),
        ]
        self.current_texture = 0
        self.scale = 0.50
        self.set_texture(self.current_texture)

    def update(self):
        self.current_texture += 1
        if self.current_texture < len(self.textures):
            self.set_texture(self.current_texture)
        else:
            self.remove_from_sprite_lists()

