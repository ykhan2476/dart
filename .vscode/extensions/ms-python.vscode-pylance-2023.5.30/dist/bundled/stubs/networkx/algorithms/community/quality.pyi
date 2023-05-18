from typing import Sequence

from itertools import combinations

from ...classes.graph import Graph
from networkx import NetworkXError
from .community_utils import is_partition
from ...utils import not_implemented_for
from ...utils.decorators import argmap

__all__ = ["coverage", "modularity", "performance", "partition_quality"]

class NotAPartition(NetworkXError):
    def __init__(self, G: Graph, collection): ...

require_partition = ...

def intra_community_edges(G: Graph, partition): ...
def inter_community_edges(G: Graph, partition): ...
def inter_community_non_edges(G: Graph, partition): ...
@require_partition
def performance(G: Graph, partition: Sequence) -> float: ...
@require_partition
def coverage(G: Graph, partition: Sequence) -> float: ...
def modularity(G: Graph, communities, weight="weight", resolution=1) -> float: ...
@require_partition
def partition_quality(G: Graph, partition: Sequence): ...