
from .base_task import Base_task
from .utils import *
import sapien

class a(Base_task):

    def setup_demo(self, is_test=False, **kwags):
        super()._init(**kwags)
        # self.load_robot()
        self.create_table_and_wall()
        # default_seed = 5
        # np.random.seed(default_seed)
        self.load_actors()

    def load_actors(self):
        # self.load_ycb_obj()
        # self.load_obj()
        self.load_ycb_urdf()

    def create_table_and_wall(self):
        # creat wall
        self.wall = create_box(
            self.scene,
            sapien.Pose(p=[0, 1, 1.5]),
            half_size=[3, 0.6, 1.5],
            color=(1, 0.9, 0.9), 
            name='wall',
        )

        # creat table
        self.table = create_table(
            self.scene,
            sapien.Pose(p=[0, 0, 0.74]),
            length=6,
            width=0.7,
            height=0.74,
            thickness=0.05,
            is_static=self.table_static
        )
    
    def visualize(self):
        while not self.viewer.closed:  # Press key q to quit
            self.scene.step()  # Simulate the world
            self.scene.update_render()  # Update the world to the renderer
            self.viewer.render()

    def load_obj(self):
        self.a, self.a_data = create_obj(
            self.scene,
            pose=sapien.Pose([0, -0.06, 0.783],[0, 0, 0.995, 0.105]),
            modelname="042_wooden_box",
            scale=[0.08, 0.08, 0.08],
        )

    def load_ycb_obj(self):
        self.a, self.a_data = create_obj_ycb(
            self.scene,
            pose=sapien.Pose([0, -0.06, 0.783],[0, 0, 0.995, 0.105]),
            modelname="002_master_chef_can",
            scale=[0.8, 0.8, 0.8],
            is_static=True
        )
