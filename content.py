from random import choice


class Content:
    def __init__(self):
        self.para1 = ("The quick brown fox jumps over the lazy dog. This sentence is commonly used in typography "
                      "because it contains every letter of the English alphabet. Typists and designers often use it "
                      "to quickly test fonts, keyboards, and layout designs. It's a simple yet effective way to "
                      "ensure that all letters are displayed correctly and in a readable manner. Practice typing this "
                      "sentence to improve your speed and accuracy!")
        self.para2 = ('Technology has revolutionized the way we live and work. From smartphones to artificial '
                      'intelligence, advancements in technology have transformed our daily lives, making tasks easier '
                      'and more efficient. With the click of a button, we can connect with people around the world, '
                      'access vast amounts of information, and even control our homes remotely. As technology '
                      'continues to evolve, it opens up new possibilities and opportunities for innovation and growth.')

        self.para3 = ('Technology has revolutionized the way we live and work. From smartphones to artificial '
                      'intelligence, advancements in technology have transformed our daily lives, making tasks easier '
                      'and more efficient. With the click of a button, we can connect with people around the world, '
                      'access vast amounts of information, and even control our homes remotely. As technology '
                      'continues to evolve, it opens up new possibilities and opportunities for innovation and growth.')

        self.para4 = ("The wonders of the natural world never cease to amaze. From the towering mountains to the deep "
                      "blue oceans, nature's beauty is unparalleled. Each season brings its own unique charm – the "
                      "vibrant colors of autumn leaves, the pristine white snow of winter, the blooming flowers of "
                      "spring, and the warm, golden rays of summer. Exploring the outdoors not only provides a sense "
                      "of adventure but also fosters a deep appreciation for the environment and the need to protect "
                      "it.")
        self.para5 = ("Reading is a window to the world, offering insights into different cultures, histories, "
                      "and perspectives. Books have the power to transport us to different times and places, "
                      "allowing us to experience adventures, solve mysteries, and learn valuable lessons. Whether "
                      "it's fiction or non-fiction, poetry or prose, reading enriches our minds and broadens our "
                      "horizons. It's a timeless activity that continues to inspire and educate people of all ages.")

    def get_content(self):
        content = choice([self.para3,
                          self.para2,
                          self.para4,
                          self.para5])
        return content
