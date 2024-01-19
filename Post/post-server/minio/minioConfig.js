const Minio = require('minio')

const minioClient = new Minio.Client({
    endPoint:'host.docker.internal',
    port: 9000,
    useSSL: false,
    // accessKey: 'YpdoMeuft1yhcM9BLIFR',
    accessKey:'OPY4RYDlrbh7gx51fiUJ',
    // secretKey: 'Q6i79iIv40guXaKmMoPa2WeSnTeffgfRQyr1xgnU'
    secretKey:'QjvNCVaN7npNomDLF1GaYFsePIvqG1SRKTvuZ3n2'
});

module.exports = minioClient;