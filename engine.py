import tank
import hiero.core

class HieroEngine(tank.platform.Engine):

    def init_engine(self):
        """
        """
        # # Copied from Nuke Engine
        self.log_debug("%s: Initializing..." % self)

        if self.context.project is None:
            # must have at least a project in the context to even start!
            raise tank.TankError("The Tank engine needs at least a project in the context "
                                 "in order to start! Your context: %s" % self.context)

    def post_app_init(self):
        """
        Called when all apps have initialized
        """
        # create menus
        tk_hiero = self.import_module("tk_hiero")
        self._menu_generator = tk_hiero.MenuGenerator(self)
        self._menu_generator.create_menu()

    def destroy_engine(self):
        """
        """
        self.log_debug("%s: Destroying..." % self)
    
    def log_debug(self, msg):
        """
        """
        msg = "Tank Debug: %s" % msg
        hiero.core.debug(msg)

    def log_info(self, msg):
        """
        """
        msg = "Tank Info: %s" % msg
        hiero.core.info(msg)

    def log_warning(self, msg):
        """
        """
        msg = "Tank Warning: %s" % msg
        hiero.core.info(msg)

    def log_error(self, msg):
        """
        """
        msg = "Tank Error: %s" % msg
        hiero.core.error(msg)
    