// generated from rosidl_generator_cpp/resource/idl__struct.hpp.em
// with input from utilities:srv/StringCommand.idl
// generated code does not contain a copyright notice

#ifndef UTILITIES__SRV__DETAIL__STRING_COMMAND__STRUCT_HPP_
#define UTILITIES__SRV__DETAIL__STRING_COMMAND__STRUCT_HPP_

#include <algorithm>
#include <array>
#include <memory>
#include <string>
#include <vector>

#include "rosidl_runtime_cpp/bounded_vector.hpp"
#include "rosidl_runtime_cpp/message_initialization.hpp"


#ifndef _WIN32
# define DEPRECATED__utilities__srv__StringCommand_Request __attribute__((deprecated))
#else
# define DEPRECATED__utilities__srv__StringCommand_Request __declspec(deprecated)
#endif

namespace utilities
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct StringCommand_Request_
{
  using Type = StringCommand_Request_<ContainerAllocator>;

  explicit StringCommand_Request_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->command = "";
    }
  }

  explicit StringCommand_Request_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : command(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->command = "";
    }
  }

  // field types and members
  using _command_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _command_type command;

  // setters for named parameter idiom
  Type & set__command(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->command = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    utilities::srv::StringCommand_Request_<ContainerAllocator> *;
  using ConstRawPtr =
    const utilities::srv::StringCommand_Request_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<utilities::srv::StringCommand_Request_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<utilities::srv::StringCommand_Request_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      utilities::srv::StringCommand_Request_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<utilities::srv::StringCommand_Request_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      utilities::srv::StringCommand_Request_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<utilities::srv::StringCommand_Request_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<utilities::srv::StringCommand_Request_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<utilities::srv::StringCommand_Request_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__utilities__srv__StringCommand_Request
    std::shared_ptr<utilities::srv::StringCommand_Request_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__utilities__srv__StringCommand_Request
    std::shared_ptr<utilities::srv::StringCommand_Request_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StringCommand_Request_ & other) const
  {
    if (this->command != other.command) {
      return false;
    }
    return true;
  }
  bool operator!=(const StringCommand_Request_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StringCommand_Request_

// alias to use template instance with default allocator
using StringCommand_Request =
  utilities::srv::StringCommand_Request_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace utilities


#ifndef _WIN32
# define DEPRECATED__utilities__srv__StringCommand_Response __attribute__((deprecated))
#else
# define DEPRECATED__utilities__srv__StringCommand_Response __declspec(deprecated)
#endif

namespace utilities
{

namespace srv
{

// message struct
template<class ContainerAllocator>
struct StringCommand_Response_
{
  using Type = StringCommand_Response_<ContainerAllocator>;

  explicit StringCommand_Response_(rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->answer = "";
    }
  }

  explicit StringCommand_Response_(const ContainerAllocator & _alloc, rosidl_runtime_cpp::MessageInitialization _init = rosidl_runtime_cpp::MessageInitialization::ALL)
  : answer(_alloc)
  {
    if (rosidl_runtime_cpp::MessageInitialization::ALL == _init ||
      rosidl_runtime_cpp::MessageInitialization::ZERO == _init)
    {
      this->answer = "";
    }
  }

  // field types and members
  using _answer_type =
    std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>>;
  _answer_type answer;

  // setters for named parameter idiom
  Type & set__answer(
    const std::basic_string<char, std::char_traits<char>, typename std::allocator_traits<ContainerAllocator>::template rebind_alloc<char>> & _arg)
  {
    this->answer = _arg;
    return *this;
  }

  // constant declarations

  // pointer types
  using RawPtr =
    utilities::srv::StringCommand_Response_<ContainerAllocator> *;
  using ConstRawPtr =
    const utilities::srv::StringCommand_Response_<ContainerAllocator> *;
  using SharedPtr =
    std::shared_ptr<utilities::srv::StringCommand_Response_<ContainerAllocator>>;
  using ConstSharedPtr =
    std::shared_ptr<utilities::srv::StringCommand_Response_<ContainerAllocator> const>;

  template<typename Deleter = std::default_delete<
      utilities::srv::StringCommand_Response_<ContainerAllocator>>>
  using UniquePtrWithDeleter =
    std::unique_ptr<utilities::srv::StringCommand_Response_<ContainerAllocator>, Deleter>;

  using UniquePtr = UniquePtrWithDeleter<>;

  template<typename Deleter = std::default_delete<
      utilities::srv::StringCommand_Response_<ContainerAllocator>>>
  using ConstUniquePtrWithDeleter =
    std::unique_ptr<utilities::srv::StringCommand_Response_<ContainerAllocator> const, Deleter>;
  using ConstUniquePtr = ConstUniquePtrWithDeleter<>;

  using WeakPtr =
    std::weak_ptr<utilities::srv::StringCommand_Response_<ContainerAllocator>>;
  using ConstWeakPtr =
    std::weak_ptr<utilities::srv::StringCommand_Response_<ContainerAllocator> const>;

  // pointer types similar to ROS 1, use SharedPtr / ConstSharedPtr instead
  // NOTE: Can't use 'using' here because GNU C++ can't parse attributes properly
  typedef DEPRECATED__utilities__srv__StringCommand_Response
    std::shared_ptr<utilities::srv::StringCommand_Response_<ContainerAllocator>>
    Ptr;
  typedef DEPRECATED__utilities__srv__StringCommand_Response
    std::shared_ptr<utilities::srv::StringCommand_Response_<ContainerAllocator> const>
    ConstPtr;

  // comparison operators
  bool operator==(const StringCommand_Response_ & other) const
  {
    if (this->answer != other.answer) {
      return false;
    }
    return true;
  }
  bool operator!=(const StringCommand_Response_ & other) const
  {
    return !this->operator==(other);
  }
};  // struct StringCommand_Response_

// alias to use template instance with default allocator
using StringCommand_Response =
  utilities::srv::StringCommand_Response_<std::allocator<void>>;

// constant definitions

}  // namespace srv

}  // namespace utilities

namespace utilities
{

namespace srv
{

struct StringCommand
{
  using Request = utilities::srv::StringCommand_Request;
  using Response = utilities::srv::StringCommand_Response;
};

}  // namespace srv

}  // namespace utilities

#endif  // UTILITIES__SRV__DETAIL__STRING_COMMAND__STRUCT_HPP_
