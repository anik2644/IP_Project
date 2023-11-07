const Minio = require('minio')

const minioClient = new Minio.Client({
    endPoint:'host.docker.internal',
    port: 9000,
    useSSL: false,
    // accessKey: 'YpdoMeuft1yhcM9BLIFR',
    accessKey:'aDXQuXYvIcve2XlDya88',
    // secretKey: 'Q6i79iIv40guXaKmMoPa2WeSnTeffgfRQyr1xgnU'
    secretKey:'v2qoHnnYqgxKQWVrCzZywYbfQk2pRYElah2IztXV'
});

module.exports = minioClient;