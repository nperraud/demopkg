from torchvision.datasets import MNIST, CIFAR100
from demopkg.conf import DATASETDIR
from torchvision import transforms
from torch.utils.data import random_split


def load_mnist():
    """Load the MNIST dataset."""

    # transforms for images
    transform = transforms.Compose(
        [transforms.ToTensor(), transforms.Normalize((0.1307,), (0.3081,))]
    )
    mnist_train = MNIST(DATASETDIR, train=True, download=True, transform=transform)
    assert len(mnist_train) == 60000
    mnist_train, mnist_val = random_split(mnist_train, [55000, 5000])

    mnist_test = MNIST(DATASETDIR, train=False, download=True, transform=transform)
    assert len(mnist_test) == 10000
    return mnist_train, mnist_val, mnist_test


def load_cifar100():
    """Load the CIFAR100 dataset."""

    # augment train and validation dataset with RandomHorizontalFlip and RandomRotation
    train_transform = transforms.Compose([
        transforms.RandomHorizontalFlip(), # randomly flip and rotate
        transforms.RandomRotation(10),
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])

    test_transform = transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))
        ])
    
    train = CIFAR100(DATASETDIR, train=True, download=True, transform=train_transform)
    assert len(train) == 50000
    train, val = random_split(train, [45000, 5000])

    test = CIFAR100(DATASETDIR, train=False, download=True, transform=test_transform)

    assert len(test) == 10000
    return train, val, test
