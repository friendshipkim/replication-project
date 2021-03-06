from torch import nn, Tensor
from bert.layer.encoder_layer import EncoderLayer


class Encoder(nn.Module):
    def __init__(
        self, n_layers: int, d_model: int, h: int, ffn_hidden: int, p_drop: float, eps: float
    ):
        super(Encoder, self).__init__()
        self.layers = nn.ModuleList(
            [EncoderLayer(d_model, h, ffn_hidden, p_drop, eps) for _ in range(n_layers)]
        )

    def forward(self, x: Tensor, src_pad_mask: Tensor) -> Tensor:
        """
        :param x: torch.Tensor, Encoder input, shape: (batch_size, max_seq_len, d_model)
        :param src_pad_mask: torch.Tensor, shape: (batch_size, seq_len)

        :return: torch.Tensor, shape: (batch_size, max_seq_len, d_model)
        """
        for i, layer in enumerate(self.layers):
            x = layer(x, src_pad_mask)
        return x
