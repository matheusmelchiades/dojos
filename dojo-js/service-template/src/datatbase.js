
const mongoose = require('mongoose')
const config = require('./config/database')

function createUrl() {

    const { host, port, database, username, password } = config

    if (config.connection.uri) {
        return config.connection.uri
    }

    if (password) {
        return `mongodb://${username}:${password}@${host}:${port}/${database}`
    }

    return `mongodb://${host}:${port}/${database}`
}

module.exports.connect = () => {

    const url = createUrl()

    return mongoose.connect(url, config.options)
}
