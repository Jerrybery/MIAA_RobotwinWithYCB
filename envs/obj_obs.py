from envs.base_task import Base_task
from envs.utils import *
from models import *
import sapien
import os
import sys 

sys.path.append("./ycb_urdfs/ycb_assets")

'''
原素材中的损坏用注释标出，用utility.py中的方法无法加载
ycb素材用了一个集成的方法
'''

class obj_obs(Base_task):
    def setup_demo(self, is_test=False,**kwags):
        super()._init(**kwags)
        default_seed = 7
        np.random.seed(default_seed)
        self.create_table_and_wall()
        # self.load_robot()
        # self.setup_planner()
        # self.load_camera()
        self.load_actors()
        self.step_lim = 400
    def load_actors(self):
        self.load_tools()
        self.load_mug()
        self.load_rack()
        self.load_shoes()
        self.load_container()
        self.load_plate()
        self.load_bottle()
        self.load_fluted_block()
        self.load_coaster()
        self.load_cup()
        self.load_cup_with_liqid()
        self.load_brush()
        # self.load_red_bottle()
        # self.load_green_bottle()
        self.load_table_tennis()
        self.load_dustpan()
        # self.load_power_drill()
        # self.load_mark_cup()
        # self.load_screwdriver()
        # self.load_fork()
        # self.load_knife()
        self.load_apple()
        self.load_cabine()
        self.load_box()
        self.load_rack()
        self.load_shoes_2()
        self.load_wooden_box()
        self.load_ycb_lib()
        pass
    
    def create_table_and_wall(self):
        # creat wall
        self.wall = create_box(
            self.scene,
            sapien.Pose(p=[0, 2.65, 1.5]),
            half_size=[3, 0.6,1.5],
            color=(1, 0.9, 0.9), 
            name='wall',
        )

        # creat table
        self.table = create_table(
            self.scene,
            sapien.Pose(p=[0, 0, 0.74]),
            length=2,
            width=4,
            height=0.78,
            thickness=0.05,
            is_static=self.table_static
        )

    def visualize(self):
        while not self.viewer.closed:  # Press key q to quit
            self.scene.step()  # Simulate the world
            self.scene.update_render()  # Update the world to the renderer
            self.viewer.render()
    
    def load_tools(self):
        id_list = [0,1,2,3,4,5,6,7,8,9]
        for id in id_list:
            self.tool, self.tool_data = create_glb(
                self.scene,
                pose=sapien.Pose([-0.95 + 0.2*id, -0.2, 0.77], [-0.378569, -0.604915, -0.379217, 0.589032]),
                modelname="tools",
                convex=False,
                model_id=id,
                is_static=True
            )

    def load_mug(self):
        id_list = [0,1,2,3,4,5,6,7,8,9]
        for id in id_list:
            self.mug, self.mug = create_glb(
                self.scene,
                pose=sapien.Pose([-0.95 + 0.15*(id+2), 0, 0.8], [-0.378569, -0.604915, -0.379217, 0.589032]),
                modelname="039_mug",
                convex=False,
                model_id=id,
                is_static=True
            )
    def load_rack(self):
        self.rack, self.rack_data = create_obj(
            self.scene,
            pose=sapien.Pose([-0.95, 0.2, 0.77], [0.5,0.5,0.5,0.5]),
            modelname="040_rack",
            scale=[0.025,0.025,0.025],
            is_static=True,
            convex=False
        )
    def load_shoes(self):
        id_list = [0,1,2,3,4,5,6,7,8,9,]
        for id in id_list:
            self.shoe, self.shoe_data = create_glb(
                self.scene,
                pose=sapien.Pose([-0.95 + 0.15*id, 0.4, 0.8],  [0.702466, 0.600326, -0.33439, -0.185295]),
                modelname="041_shoes",
                convex=False,
                model_id=id,
                is_static=True
            )
    def load_shoes_2(self):
        id_list = [10, 11, 12, 13, 14, 15]
        for id in id_list:
            self.shoe, self.shoe_data = create_glb(
                self.scene,
                pose=sapien.Pose([-.1+ 0.15*(id-10), -0.73, 0.8],  [0.702466, 0.600326, -0.33439, -0.185295]),
                modelname="041_shoes",
                convex=False,
                model_id=id,
                is_static=True
            )
    def load_container(self):
        id_list = [0,1,2,3,4,5,6,7,8,9]
        for id in id_list:
            self.container, self.container_data = create_glb(
                self.scene,
                pose=sapien.Pose([-0.95 + 0.16*(id+1), 0.2, 0.8], [0.702466, 0.600326, -0.33439, -0.185295]),
                modelname="002_container",
                convex=False,
                model_id=id,
                is_static=True,
                scale=[0.88,0.88,0.88]
            )
    def load_plate(self):
        self.plate, _ = create_glb(
            self.scene,
            pose=sapien.Pose([-0.95, 0, 0.78], [0.5,0.5,0.5,0.5]),
            modelname="003_plate",
            scale=[0.035,0.035,0.035],
            convex=False,
            is_static=True
        )
    def load_bottle(self):
        id_list_1 = [0,1,2,3,4,5,6,7,8,9,10]
        for id in id_list_1:
            self.bottle, self.bottle_data = create_glb(
                self.scene,
                pose=sapien.Pose([-0.95 + 0.15*id, 0.6, 0.88], [0.707107, 0.707107, -0, 0]),
                modelname="001_bottles",
                convex=False,
                model_id=id,
                is_static=True
            )
        id_list_2 = [11,12,13,14,15,16,17,18,19,20,21]
        for id in id_list_2:
            self.bottle, self.bottle_data = create_glb(
                self.scene,
                pose=sapien.Pose([-0.95 + 0.15*(id-11), 0.8, 0.88], [0.707107, 0.707107, -0, 0]),
                modelname="001_bottles",
                convex=True,
                model_id=id,
                is_static=True
            )
    def load_fluted_block(self):
        id_list = [0, 1]
        for id in id_list:
            self.fluid_block, self.fluid_block_data = create_obj(
                self.scene,
                pose=sapien.Pose([-0.95 + 0.15 * (id+10), 0.4, 0.8], [0.5, 0.5, 0.5, 0.5]),
                modelname="004_fluted_block",
                scale=[0.025, 0.025, 0.025],
                model_id=id,
                is_static=True,
                convex=False
            )
    def load_coaster(self):
        self.coaster, _ = create_obj(
            self.scene,
            pose=sapien.Pose([0.7, 0.2, 0.75], [0.5, 0.5, 0.5, 0.5]),
            modelname="019_coaster",
            scale=[0.035, 0.035, 0.035],
            convex=True,
            is_static=True
        )
    def load_cup(self):
        self.cup_1, self.cup_1_data = create_obj(
            self.scene,
            pose=sapien.Pose([-0.95, -0.4, 0.83], [0.5, 0.5, 0.5, 0.5]),
            modelname="022_cup",
            scale=[0.022, 0.022, 0.022],
            convex=True,
            is_static=True
        )
        self.cup_2, self.cup_2_data = create_obj(
            self.scene,
            pose=sapien.Pose([-0.95 + 0.225, -0.4, 0.83], [0.5, 0.5, 0.5, 0.5]),
            modelname="022_cup",
            scale=[0.022, 0.022, 0.022],
            convex=True,
            is_static=True
        )
        # self.cup_3, self.cup_3_data = create_obj( # 棍母水杯
        #     self.scene,
        #     pose=sapien.Pose([-0.95 + 0.15*2, -0.4, 0.82], [0.5, 0.5, 0.5, 0.5]),
        #     modelname="022_cup",
        #     scale=[0.025, 0.025, 0.025],
        #     convex=True,
        #     model_id=2,
        #     is_static=True
        # )
    def load_cup_with_liqid(self):
        self.cup_4, self.cup_4_data = create_obj( 
            self.scene,
            pose=sapien.Pose([-0.95 + 0.15*3, -0.4, 0.83], [0.5, 0.5, 0.5, 0.5]),
            modelname="022_cup_with_liquid",
            scale=[0.09, 0.09, 0.09],
            convex=False,
            is_static=True
        )
    def load_brush(self):
        self.brush, _ = create_glb(
            self.scene,
            pose=sapien.Pose([-0.35, -0.4, 0.77], [-0.165969, 0.687353, -0.165969, -0.687353]),
            modelname="024_brush",
            scale=[0.02, 0.02, 0.02],
            convex=False,
            is_static=True
        )
    # def load_red_bottle(self): # 这就是可口可乐，在bottles中出现过了
    #     self.red_bottle, self.red_bottle_data = create_obj(
    #         self.scene,
    #         pose=sapien.Pose([-0.2, -0.4, 0.88], [0.707107, 0.707107, -0, 0]),
    #         modelname="025_red_bottle",
    #         convex=True,
    #         scale=[0.14, 0.14, 0.14],
    #         is_static=True
    #     )
    # def load_green_bottle(self): # 这就是雪碧，在bottles中出现过了
    #     self.green_bottle, self.green_bottle_data = create_obj(
    #         self.scene,
    #         pose=sapien.Pose([-0.2, -0.4, 0.88], [0.707107, 0.707107, -0, 0]),
    #         modelname="026_green_bottle",
    #         convex=True,
    #         scale=[0.14, 0.14, 0.14],
    #         is_static=True
    #     )
    def load_table_tennis(self):
        self.table_tennis, _ = create_obj(
            self.scene,
            pose=sapien.Pose([0, -0.4, 0.766379], [0.5, 0.5, 0.5, 0.5]),
            modelname="027_table_tennis",
            scale=[0.02, 0.02, 0.02],
            convex=False,
            is_static=True
        )
    def load_dustpan(self):
        self.dustpan, self.dustpan_data = create_obj(
            self.scene,
            pose=sapien.Pose([-0.1, -0.4, 0.78], [0.5, 0.5, 0.5, 0.5]),
            modelname="028_dustpan",
            scale=[0.8, 0.8, 0.8],
            convex=False,
            is_static=True
        )
    # def load_power_drill(self): # 这电钻也在tool中有,但是加载不出来,是棍母
    #     self.power_drill, self.power_drill_data = create_glb(
    #         self.scene,
    #         pose=sapien.Pose([0.3, -0.4, 0.78], [0.5, 0.5, 0.5, 0.5]),
    #         modelname="030_power_drill",
    #         scale=[0.02, 0.02, 0.02],
    #         convex=True,
    #         is_static=True
    #     )
    # def load_mark_cup(self): # 莫名其妙加载不出来,也是棍母
    #     self.mark_cup, self.mark_cup_data = create_glb(
    #         self.scene,
    #         pose=sapien.Pose([-0.95 + 0.15*3, -0.4, 0.83], [0.5, 0.5, 0.5, 0.5]),
    #         modelname="031_mark_cup",
    #         scale=[0.09, 0.09, 0.09],
    #         convex=False,
    #         is_static=True
    #     )
    # def load_screwdriver(self): # gunmu
    #     self.screwdriver, _ = create_glb(
    #         self.scene,
    #         pose=sapien.Pose([-0.95 + 0.15*3, -0.4, 0.83], [0.5, 0.5, 0.5, 0.5]),
    #         modelname="032_screwdriver",
    #         scale=[0.02, 0.02, 0.02],
    #         convex=True,
    #         is_static=True
    #     )
    # def load_fork(self): # gunmu
    #     self.fork, _ = create_glb(
    #         self.scene,
    #         pose=sapien.Pose([-0.95 + 0.15*3, -0.4, 0.83], [0.5, 0.5, 0.5, 0.5]),
    #         modelname="033_fork",
    #         scale=[0.02, 0.02, 0.02],
    #         convex=True,
    #         is_static=True
    #     )
    # def load_knife(self): # gunmu
    #     self.knife, _ = create_glb(
    #         self.scene,
    #         pose=sapien.Pose([-0.95 + 0.15*3, -0.4, 0.83], [0.5, 0.5, 0.5, 0.5]),
    #         modelname="034_knife",
    #         scale=[0.02, 0.02, 0.02],
    #         convex=True,
    #         is_static=True
    #     )
    def load_apple(self):
        self.apple, _ = create_obj(
            self.scene,
            pose=sapien.Pose([0.1, -0.4, 0.778257], [0.707107, 0, 0, 0.707107]),
            modelname="035_apple",
            scale=[0.02, 0.02, 0.02],
            convex=True,
            is_static=True
        )
    def load_cabine(self):
        self.cabine, _ = create_urdf_obj(
            self.scene,
            pose=sapien.Pose([0.5, -0.45, 0.82], [0.5, 0.5, 0.5, 0.5]),
            modelname="036_cabine",
            scale=0.3)
    def load_box(self):
        self.box, _ = create_urdf_obj(
            self.scene,
            pose=sapien.Pose([-.5, -0.7, 0.8], [0.707107, 0, 0, 0.707107]),
            modelname="037_box",
            scale=0.3)
    def load_wooden_box(self):
        self.wooden_box, _ = create_obj(
            self.scene,
            pose=sapien.Pose([0.482208, -0.454753, 1], [0.707107, 0.707107, 0, 0]),
            modelname="042_wooden_box",
            scale=[0.1, 0.1, 0.1],
            is_static=True
            )
    def _generate_random_quaternion(self,seed=None):
        if seed is not None:
            np.random.seed(seed)
        quaternion = np.random.randn(4)
        quaternion = quaternion / np.linalg.norm(quaternion)
        return quaternion

    def load_ycb_lib(self):
        """
        动态加载 ycb_urdfs/ycb_assets 文件夹中的所有 URDF 文件。
        """
        ycb_assets_path = "./ycb_urdfs/ycb_assets"
        urdf_files = sorted([d for d in os.listdir(ycb_assets_path) if os.path.isdir(os.path.join(ycb_assets_path, d))])

        c = 0
        r = 0
        obj_cnt = 0
        init_y = -1.2
        init_z = .74
        for urdf_file in urdf_files:
            c += 1
            obj_cnt += 1
            if obj_cnt > 20:
                init_y = .8
                init_z = .77
            if obj_cnt > 60:
                break
            pose = [-0.95 + 0.15 * c, init_y + 0.23 * r, init_z]
            if c > 11:
                c = 0
                r += 1
            modelname = os.path.splitext(urdf_file)[0]
            self.disp_ycb_object(modelname, pose=pose)

    def disp_ycb_object(self, modelname, pose):
        create_obj_ycb(
            self.scene,
            is_static= True,
            pose=sapien.Pose(pose, [1, 0, 0, 0]),
            modelname=modelname,
            scale=(1.1,1.1,1.1)
        )