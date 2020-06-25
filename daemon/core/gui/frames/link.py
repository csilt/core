import tkinter as tk
from typing import TYPE_CHECKING

from core.gui.frames.base import DetailsFrame, InfoFrameBase
from core.gui.utils import bandwidth_text

if TYPE_CHECKING:
    from core.gui.app import Application
    from core.gui.graph.edges import CanvasEdge


class EdgeInfoFrame(InfoFrameBase):
    def __init__(
        self, master: tk.BaseWidget, app: "Application", edge: "CanvasEdge"
    ) -> None:
        super().__init__(master, app)
        self.edge: "CanvasEdge" = edge

    def draw(self) -> None:
        self.columnconfigure(0, weight=1)
        link = self.edge.link
        options = link.options
        src_canvas_node = self.app.core.canvas_nodes[link.node1_id]
        src_node = src_canvas_node.core_node
        dst_canvas_node = self.app.core.canvas_nodes[link.node2_id]
        dst_node = dst_canvas_node.core_node

        frame = DetailsFrame(self)
        frame.grid(sticky="ew")
        frame.add_detail("Source", src_node.name)
        iface1 = link.iface1
        if iface1:
            mac = iface1.mac if iface1.mac else "auto"
            frame.add_detail("MAC", mac)
            ip4 = f"{iface1.ip4}/{iface1.ip4_mask}" if iface1.ip4 else ""
            frame.add_detail("IP4", ip4)
            ip6 = f"{iface1.ip6}/{iface1.ip6_mask}" if iface1.ip6 else ""
            frame.add_detail("IP6", ip6)

        frame.add_separator()
        frame.add_detail("Destination", dst_node.name)
        iface2 = link.iface2
        if iface2:
            mac = iface2.mac if iface2.mac else "auto"
            frame.add_detail("MAC", mac)
            ip4 = f"{iface2.ip4}/{iface2.ip4_mask}" if iface2.ip4 else ""
            frame.add_detail("IP4", ip4)
            ip6 = f"{iface2.ip6}/{iface2.ip6_mask}" if iface2.ip6 else ""
            frame.add_detail("IP6", ip6)

        if link.HasField("options"):
            frame.add_separator()
            bandwidth = bandwidth_text(options.bandwidth)
            frame.add_detail("Bandwidth", bandwidth)
            frame.add_detail("Delay", f"{options.delay} us")
            frame.add_detail("Jitter", f"\u00B1{options.jitter} us")
            frame.add_detail("Loss", f"{options.loss}%")
            frame.add_detail("Duplicate", f"{options.dup}%")
