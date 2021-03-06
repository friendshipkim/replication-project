from torch import nn
from torch import Tensor


class PointwiseFeedForward(nn.Module):
    def __init__(self, d_model: int, ffn_hidden: int, p_drop: float):
        super(PointwiseFeedForward, self).__init__()
        self.fc_1 = nn.Linear(d_model, ffn_hidden)
        self.gelu = nn.GELU()
        self.fc_2 = nn.Linear(ffn_hidden, d_model)

    def forward(self, x: Tensor) -> Tensor:
        """
        :param x: torch.Tensor, shape: (batch_size, max_seq_len, d_model)
        :return: torch.Tensor, shape: (batch_size, max_seq_len, d_model)
        """
        x = self.fc_1(x)
        x = self.relu(x)
        x = self.fc_2(x)

        return x
