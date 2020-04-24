const model = require('model')

module.exports.get = async (req, res) => {

    try {
        const { params } = req

        const data = await model.findSomeThing(params)

        return res.json(data)
    } catch (err) {
        console.log(err.message)

        return err
    }
}

module.exports.post = async (req, res) => {

    try {
        const { params } = req

        const data = await model.insertSomething(params)

        return res.json(data)
    } catch (err) {
        console.log(err.message)

        return err
    }
}

module.exports.put = async (req, res) => {

    try {
        const { params } = req

        const data = await model.updateSomething(params)

        return res.json(data)
    } catch (err) {
        console.log(err.message)

        return err
    }
}

module.exports.delete = async (req, res) => {

    try {
        const { params } = req

        const data = await model.removeSomething(params)

        return res.json(data)
    } catch (err) {
        console.log(err.message)

        return err
    }
}
