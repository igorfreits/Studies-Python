import re


class CalcIPv4:
    """
    Faz o cálculo de redes IPv4

    Modo de uso 1:
    calc_ipv4 = CalcIPv4(ip='192.168.0.128', prefixo=10)

    Modo de uso 2:
    calc_ipv4 = CalcIPv4(ip='192.168.0.128', mascara='255.255.255.0')
    """

    def __init__(self, ip, mask=None, prefix=None):
        self.ip = ip
        self.mask = mask
        self.prefix = prefix

        if mask is None and prefix is None:
            raise ValueError('Precisa enviar máscara ou prefixo')

        if mask and prefix:
            raise ValueError('Precisa enviar máscara ou prefixo, não ambos.')

        self._set_broadcast()
        self._set_network()

    @property
    def network(self):
        return self._network

    @property
    def broadcast(self):
        return self._broadcast

    @property
    def number_ips(self):
        return self._get_number_ips()

    @property
    def ip(self):
        return self._ip

    @property
    def mask(self):
        return self._mask

    @property
    def prefix(self):
        if self._prefix is None:
            return

        return self._prefix

    @ip.setter
    def ip(self, value):
        if not self._validate_ip(value):
            raise ValueError('IP inválido.')

        self._ip = value
        self._ip_bin = self._ip_to_bin(value)

    @mask.setter
    def mask(self, value):
        if not value:
            return

        if not self._validate_ip(value):
            raise ValueError('Máscara inválida.')

        self._mask = value
        self._mask_bin = self._ip_to_bin(value)

        if not hasattr(self, 'prefixo'):
            self.prefix = self._mask_bin.count('1')

    @prefix.setter
    def prefix(self, value):
        if value is None:
            return

        try:
            value = int(value)
        except:
            raise ValueError('Prefixo precisa ser um inteiro.')

        if value > 32 or value < 0:
            raise TypeError('Prefixo precisa ter 32Bits.')

        self._prefix = value
        self._mask_bin = (value * '1').ljust(32, '0')

        if not hasattr(self, 'mask'):
            self.mask = self._bin_to_ip(self._mask_bin)

    @staticmethod
    def _validate_ip(ip):
        regexp = re.compile(
            r'^([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3}).([0-9]{1,3})$'
        )

        if regexp.search(ip):
            return True

    @staticmethod
    def _ip_to_bin(ip):
        blocks = ip.split('.')
        blocks_bin = [bin(int(block))[2:].zfill(8) for block in blocks]
        blocks_bin_str = ''.join(blocks_bin)
        qtd_bits = len(blocks_bin_str)

        if qtd_bits > 32:
            raise ValueError('IP ou máscara tem mais que 32 bits.')

        return blocks_bin_str

    @staticmethod
    def _bin_to_ip(ip):
        n = 8
        blocks = [str(int(ip[i:n + i], 2)) for i in range(0, 32, n)]
        return '.'.join(blocks)

    def _set_broadcast(self):
        host_bits = 32 - self.prefix
        self._broadcast_bin = self._ip_bin[:self.prefix] + (host_bits * '1')
        self._broadcast = self._bin_to_ip(self._broadcast_bin)
        return self._broadcast

    def _set_network(self):
        host_bits = 32 - self.prefix
        self._network_bin = self._ip_bin[:self.prefix] + (host_bits * '0')
        self._network = self._bin_to_ip(self._network_bin)
        return self._network

    def _get_number_ips(self):
        return 2 ** (32 - self.prefix)


    # Com prefixo
calc_ipv4_1 = CalcIPv4(ip='192.168.0.128', prefix=30)

print(f'IP: {calc_ipv4_1.ip}')
print(f'Máscara: {calc_ipv4_1.mask}')
print(f'Rede: {calc_ipv4_1.network}')
print(f'Broadcast: {calc_ipv4_1.broadcast}')
print(f'Prefixo: {calc_ipv4_1.prefix}')
print(f'Número de IPs da rede: {calc_ipv4_1.number_ips}')

print('#' * 80)

# Com máscara
calc_ipv4_2 = CalcIPv4(ip='192.168.0.128', mask='255.255.255.192')

print(f'IP: {calc_ipv4_2.ip}')
print(f'Máscara: {calc_ipv4_2.mask}')
print(f'Rede: {calc_ipv4_2.network}')
print(f'Broadcast: {calc_ipv4_2.broadcast}')
print(f'Prefixo: {calc_ipv4_2.prefix}')
print(f'Número de IPs da rede: {calc_ipv4_2.number_ips}')
